#!/usr/bin/env python3

import sys
import re 

def ler_arquivo_hex(caminho):
    with open(caminho, "r") as f:
        dados = f.read()
    limpo = re.sub(r'[^0-9a-fA-F]', '', dados)
    return bytes.fromhex(limpo)

def para_ip(b):
        return ".".join(str(x) for x in b)

def analisar_ipv4(pkt):
        versao = pkt[0] >> 4
        ihl = (pkt[0] & 0x0F) * 4
        tamanho_total = int.from_bytes(pkt[2:4], "big")
        ttl = pkt[9]
        protocolo = pkt[9]
        origem = para_ip(pkt[12:16])
        destino = para_ip(pkt[16:20])
        return ihl, {
                "versão": versao,
                "ihl" : ihl,
                "tamanho_total": tamanho_total,
                "ttl": ttl,
                "protocolo": protocolo,
                "ip_origem": origem,
                "ip_destino": destino
        }

def analisar_transporte(protocolo, dados):
        protocolo_ipv4 = {
                1: "ICMP",
                2: "IGMP",
                6: "TCP",
                17: "UDP",
                41: "IPv6",
                47: "GRE",
                50: "ESP",
                51: "AH",
                58: "ICMPv6",
                89: "OSPF",
                132: "SCTP"
        }

        nome_protocolo = protocolo_ipv4.get(protocolo, "Desconhecido")

        if protocolo not in [6, 17]:
                return nome_protocolo, {}
        
        porta_origem = int.from_bytes(dados[0:2], "big")
        porta_destino = int.from_bytes(dados[2:4], "big")

        servicos_por_porta = {
                20: "FTP-DATA",
                21: "FTP",
                22: "SSH",
                23: "TELNET",
                25: "SMTP",
                53: "DNS",
                67: "DHCP-Server",
                68: "DHCP-Client",
                69: "TFTP",
                80: "HTTP",
                110: "POP3",
                123: "NTP",
                143: "IMAP",
                161: "SNMP",
                389: "LDAP",
                443: "HTTPS",
                445: "SMB",
                631: "IPP",
                993: "IMAPS",
                995: "POP3S",
                3306: "MySQL",
                3389: "RDP",
                5432: "PostgreSQL",
                5900: "VNC",
                6379: "Redis",
                8080: "HTTP-ALT"
        }

        servico_origem = servicos_por_porta.get(porta_origem, "Desconhecido")
        servico_destino = servicos_por_porta.get(porta_destino, "Desconhecido")

        resposta = {
                "porta_origem": porta_origem,
                "porta_destino": porta_destino,
                "servico_origem": servico_origem,
                "servico_destino": servico_destino
        }

        if protocolo == 6: 
                flags_byte = dados[13]

                def decodificar_flags_tcp(flags_byte):
                        flags = {
                                "FIN": 0x01,
                                "SYN": 0x02,
                                "RST": 0x04,
                                "PSH": 0x08,
                                "ACK": 0x10,
                                "URG": 0x20,
                                "ECE": 0x40,
                                "CWR": 0x80
                        }
                        return [nome for nome, valor in flags.items() if flags_byte & valor]

                resposta["flags"] = decodificar_flags_tcp(flags_byte)

        return nome_protocolo, resposta

def detectar_ethernet(pkt):
        if pkt[0] == 0x45:
                return 0
        tipo_eth = int.from_bytes(pkt[12:14], "big")
        if tipo_eth == 0x0800:
                return 14
        return 0

def main():
        if len(sys.argv) != 2:
                print("Uso: decoder.py <arquivo_hex>")
                sys.exit(1)

        pkt = ler_arquivo_hex(sys.argv[1])

        deslocamento = detectar_ethernet(pkt)
        pkt = pkt[deslocamento:]

        try:
            ihl, ipv4 = analisar_ipv4(pkt)
        except:
            print("Não é um cabeçalho IPv4 válido")
            sys.exit(1)

        print("\nCABEÇALHO IPv4")
        for campo, valor in ipv4.items():
               print(f"{campo}: {valor}")

        protocolo = ipv4["protocolo"]
        nome_transporte, transporte = analisar_transporte(protocolo, pkt[ihl:ihl+20])

        print(f"\nTRANSPORTE ({nome_transporte})")
        for campo, valor in transporte.items():
               print(f"{campo}: {valor}")

        payload = pkt[ihl+20:]
        if payload:
               ascii_printavel = '' .join(chr(byte) if 32 <= byte <= 126 else '.' for byte in payload)
               print(f"\nPAYLOAD (ASCII)") 
               print(ascii_printavel)

        print()

if __name__ == "__main__":
    main()
