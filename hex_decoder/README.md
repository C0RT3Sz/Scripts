# 🧪 Packet Decoder – IPv4 / TCP / UDP

Este projeto consiste em um **script em Python para decodificação automática de pacotes de rede em hexadecimal**, interpretando manualmente os campos dos protocolos **IPv4** e **TCP/UDP**, além de exibir o payload em ASCII quando presente.

O script foi criado como uma **ferramenta de apoio ao estudo de redes e segurança ofensiva**, especialmente durante os **módulos iniciais da Desec Security**, onde há grande volume de exercícios envolvendo **conversão manual de bytes, offsets, cabeçalhos e flags**.

O objetivo principal é **eliminar o trabalho repetitivo e manual**, permitindo focar na **análise e entendimento do protocolo**, e não apenas na conversão byte a byte.

---

## 🎯 Objetivo do código

* Automatizar a conversão de pacotes em hexadecimal para informações legíveis
* Facilitar o estudo de protocolos de rede em baixo nível
* Ajudar na interpretação de tráfego em exercícios de CTF e laboratórios
* Reduzir erros humanos em conversões manuais
* Servir como ferramenta educacional para entendimento real de IPv4 e TCP

---

## 📌 Para que este script serve

Este script **não é um sniffer**, nem uma ferramenta de captura de tráfego. Ele serve para:

* Analisar pacotes já capturados ou fornecidos em formato hexadecimal
* Decodificar manualmente:

  * Cabeçalho IPv4
  * Protocolo de transporte (TCP ou UDP)
  * Portas de origem e destino
  * Serviços comuns associados às portas
  * Flags TCP
  * Payload em ASCII

É ideal para:

* Estudo de redes
* Pentest
* CTFs
* Forense básica
* Treinamento em segurança ofensiva

---

## ⚙️ Como funciona

1. O script lê um arquivo contendo um pacote em hexadecimal
2. Remove espaços, quebras de linha e caracteres inválidos
3. Converte os dados para bytes
4. Analisa o cabeçalho IPv4:

   * Versão
   * IHL
   * Tamanho total
   * TTL
   * Protocolo
   * IP de origem
   * IP de destino
5. Identifica o protocolo de transporte
6. Se for TCP ou UDP:

   * Extrai portas
   * Associa serviços conhecidos
7. Se for TCP:

   * Decodifica as flags
8. Exibe o payload em ASCII, quando possível

---

## ▶️ Como utilizar

1. Crie um arquivo de texto contendo o pacote em hexadecimal
2. Execute o script passando o arquivo como argumento

Exemplo de execução:
```
./decoder.py hex.txt
```

---

## 📤 Exemplo de saída

Ao executar o script com um pacote válido, a saída será semelhante a:
```
CABEÇALHO IPv4
versão: 4
ihl: 20
tamanho_total: 52
ttl: 6
protocolo: 6
ip_origem: 192.168.1.100
ip_destino: 192.168.1.200

TRANSPORTE (TCP)
porta_origem: 80
porta_destino: 54321
servico_origem: HTTP
servico_destino: Desconhecido
flags: ['PSH', 'ACK']

PAYLOAD (ASCII)
Hello!
```

---

## 🧾 Exemplo de hexadecimal analisado

O pacote utilizado no exemplo acima:

45 00 00 34 12 34 40 00 40 06 00 00
c0 a8 01 64
c0 a8 01 c8
00 50 d4 31
12 34 56 78
00 00 00 00
50 18 40 00 00 00 00 00
48 65 6c 6c 6f 21

---

## ⚠️ Aviso legal

Este código foi desenvolvido **exclusivamente para fins educacionais**.

* Não utilize este script para interceptar, analisar ou manipular tráfego de redes sem autorização
* O autor não se responsabiliza pelo uso indevido da ferramenta
* Utilize apenas em ambientes controlados, laboratórios, CTFs ou redes onde você possua permissão explícita

O uso indevido pode violar leis locais, políticas de segurança e termos de serviço.

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Manipulação de bytes
* Análise manual de protocolos de rede

---

## 📚 Contexto

Este script faz parte de um repositório pessoal de **scripts de estudo em segurança ofensiva**, criados durante a formação em **Pentest e Red Team**, com foco em:

* Redes
* Protocolos
* Automação
* CTFs
* Desec Security
