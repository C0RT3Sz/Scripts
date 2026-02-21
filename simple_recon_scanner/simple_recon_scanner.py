import ipaddress
import socket
from datetime import datetime

def main():
    print("\n=== Simple Recon Scanner ===\n")

    modo = input("Modo de uso (1 = Manual | 2 = Arquivo): ").strip()

    if modo == "1":
        lista_alvos = receber_alvos()
    elif modo == "2":
        caminho = input("Caminho do arquivo: ").strip()
        lista_alvos = ler_wordlist(caminho)
    else:
        print("Modo inválido.")
        return

    if not lista_alvos:
        print("Nenhum alvo válido encontrado.")
        return

    processar_alvos(lista_alvos)


def processar_alvos(lista_alvos):
    portas_globais = None

    if len(lista_alvos) > 1:
        portas_globais = receber_portas()
        usar_mesmas = input("Usar essas portas para todos os hosts? (y/n): ").lower()

        if usar_mesmas != "y":
            portas_globais = None

    for alvo in lista_alvos:

        info_alvo = identificar_alvo(alvo)

        if not info_alvo["ip"]:
            salvar_resultado(f"Erro: não foi possível resolver {alvo}")
            continue

        if portas_globais:
            lista_portas = portas_globais
        else:
            lista_portas = receber_portas()

        resultados = testar_conexoes(info_alvo["ip"], lista_portas)

        for porta, status in resultados:
            mensagem = formatar_saida(info_alvo, porta, status)
            salvar_resultado(mensagem)


def identificar_alvo(alvo):
    resultado = {
        "entrada": alvo,
        "tipo": None,
        "ip": None,
        "hostname": None
    }

    if validar_ip(alvo):
        resultado["tipo"] = "ip"
        resultado["ip"] = alvo

        # Tenta resolver nome reverso
        try:
            hostname = socket.gethostbyaddr(alvo)[0]
            resultado["hostname"] = hostname
        except socket.herror:
            resultado["hostname"] = None

    else:
        resultado["tipo"] = "dominio"
        ip = resolver_dns(alvo)
        resultado["ip"] = ip
        resultado["hostname"] = alvo

    return resultado


def formatar_saida(info_alvo, porta, status):

    if info_alvo["tipo"] == "ip":
        if info_alvo["hostname"]:
            base = f"IP do host {info_alvo['hostname']}"
        else:
            base = "IP informado"
    else:
        base = f"IP resolvido para {info_alvo['entrada']}"

    return f"{base}: {info_alvo['ip']}:{porta} está {status}"


def receber_alvos():
    entrada = input("Digite domínios ou IPs separados por vírgula: ")
    return [item.strip() for item in entrada.split(",") if item.strip()]


def resolver_dns(alvo):
    try:
        return socket.gethostbyname(alvo)
    except socket.gaierror:
        return None


def validar_ip(alvo):
    try:
        ipaddress.ip_address(alvo)
        return True
    except ValueError:
        return False


def ler_wordlist(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return [linha.strip() for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []


def receber_portas():
    entrada = input(
        "Digite as portas separadas por vírgula (Enter = padrão 80): "
    ).strip()

    if not entrada:
        return [80]

    lista_portas = []

    for item in entrada.split(","):
        item = item.strip()
        if not item:
            continue

        try:
            lista_portas.append(int(item))
        except ValueError:
            print(f"{item} não é uma porta válida e será ignorada.")

    return lista_portas if lista_portas else [80]


def testar_conexoes(ip, lista_portas):
    resultados = []

    for porta in lista_portas:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(3)
            client.connect((ip, porta))
            status = "ativo"
        except (socket.timeout, socket.error):
            status = "inativo"
        finally:
            client.close()

        resultados.append((porta, status))

    return resultados


def salvar_resultado(mensagem):
    timestamp = datetime.now().strftime("(%H:%M:%S | %d/%m/%Y)")

    linha = f"{timestamp} {mensagem}"

    print(linha)

    with open("resultados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(linha + "\n")


if __name__ == "__main__":
    main()
