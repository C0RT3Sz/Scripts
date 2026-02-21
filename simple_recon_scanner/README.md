# 🔎 Simple Recon Scanner – DNS & TCP Port Checker

Este projeto consiste em um script em Python para **resolução de domínios e teste de portas TCP**, permitindo verificar rapidamente se um host está ativo e quais portas estão acessíveis.

O script foi desenvolvido como parte do meu processo de aprendizado em Python aplicado a redes e segurança ofensiva, com foco em automação de tarefas básicas de reconhecimento.

O objetivo principal é consolidar conceitos fundamentais como:

* Manipulação de sockets
* Resolução DNS
* Validação de IPs
* Tratamento de exceções
* Estruturação e organização de código

---

# 🎯 Objetivo do código

* Resolver domínios para IP
* Identificar se uma entrada é IP ou domínio
* Realizar teste de portas TCP
* Indicar se a porta está ativa ou inativa
* Registrar resultados com timestamp em arquivo
* Servir como ferramenta prática de estudo em reconhecimento de rede

---

# 📌 Para que este script serve

Este script não é um scanner avançado como Nmap.

Ele foi criado para:

* Treinar lógica de programação aplicada a redes
* Automatizar testes simples de conectividade
* Entender funcionamento de sockets TCP
* Praticar organização e estruturação de código

É ideal para:

* Estudo de redes
* Laboratórios de segurança
* Treinamento em Python
* Entendimento básico de reconhecimento de infraestrutura

---

# ⚙️ Como funciona

O script pode operar de duas formas:

### 1️⃣ Modo Manual

O usuário informa:

* IPs ou domínios separados por vírgula
* Portas para teste (ou usa padrão 80)

### 2️⃣ Modo Arquivo

O usuário fornece:

* Um arquivo contendo lista de alvos (um por linha)

---

### Processo interno:

1. Identifica se a entrada é IP ou domínio
2. Caso seja domínio:

   * Realiza resolução DNS
3. Caso seja IP:

   * Tenta realizar reverse DNS (quando possível)
4. Testa conexão TCP nas portas informadas
5. Registra o resultado com data e hora
6. Salva automaticamente em:

```
resultados.txt
```

---

# ▶️ Como utilizar

Execute o script com Python 3:

```
python3 simple_recon_scanner.py
```

Escolha o modo desejado:

```
Modo de uso (1 = Manual | 2 = Arquivo):
```

Se manual:

* Digite os alvos separados por vírgula

Exemplo:

```
google.com, 8.8.8.8
```

Depois informe as portas:

```
80,443,8080
```

---

# 📤 Exemplo de saída

```
(14:22:10 | 15/02/2026) IP resolvido para google.com: 142.250.78.14:80 está ativo
(14:22:11 | 15/02/2026) IP informado: 8.8.8.8:443 está ativo
```

---

# 🧾 Arquivo de saída

Todos os resultados são registrados automaticamente em:

```
resultados.txt
```

Incluindo:

* Timestamp
* Host analisado
* IP
* Porta
* Status (ativo/inativo)

---

# 🛠️ Tecnologias utilizadas

* Python 3
* Biblioteca `socket`
* Biblioteca `ipaddress`
* Manipulação de arquivos
* Tratamento de exceções
* Estruturação modular com funções

---

# 📚 Contexto

Este script faz parte de um repositório pessoal de ferramentas desenvolvidas durante meu processo de evolução em Python aplicado à segurança ofensiva.

Ele integra uma série de projetos intermediários criados com o objetivo de sair do nível iniciante e construir base sólida em:

* Redes
* Automação
* Reconhecimento
* Organização de código
* Boas práticas em Python

Este projeto representa uma evolução em relação aos scripts iniciais, já incorporando melhorias estruturais e refatoração consciente.

---

# ⚠️ Aviso legal

Este código foi desenvolvido exclusivamente para fins educacionais.

Utilize apenas em ambientes autorizados, laboratórios ou redes onde você possua permissão explícita.

O uso indevido pode violar leis locais e políticas de segurança.

O autor não se responsabiliza por uso inadequado da ferramenta.

