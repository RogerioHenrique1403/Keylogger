Este repositório contém uma Prova de Conceito (PoC) de um **Keylogger simples desenvolvido em Python**. O projeto foi criado exclusivamente para **fins educacionais e de pesquisa em cibersegurança**, com o objetivo de demonstrar como funcionam as ameaças de captura de dados e como os analistas de segurança podem detetar e mitigar este tipo de comportamento malicioso (Engenharia Reversa / Análise de Malware).

---

## ⚠️ AVISO DE ISENÇÃO DE RESPONSABILIDADE (DISCLAIMER)

> **IMPORTANTE:** Este software foi desenvolvido estritamente para fins de educação e testes de segurança autorizados. O uso deste código para monitorizar dispositivos sem o consentimento explícito e por escrito do proprietário é estritamente ilegal e viola as leis de privacidade nacionais e internacionais. O autor não se responsabiliza por quaisquer danos ou utilizações indevidas deste código. **Use com responsabilidade.**

---

## 🛠️ Funcionalidades Demonstradas

- **Captura de Input:** Monitorização e registo das teclas premidas no teclado em tempo real.
- **Armazenamento Local:** Gravação dos dados capturados num arquivo de texto local (ex: `log.txt`) para posterior análise.
- **Tratamento de Teclas Especiais:** Identificação de teclas de controlo (como `Space`, `Enter`, `Backspace`, etc.) para manter o texto legível.

## 🚀 Como Executar (Ambiente de Testes)

### Pré-requisitos
Certifique-se de que tem o Python 3 instalado na sua máquina. Irá precisar também da biblioteca `pynput` para capturar os eventos do teclado.

### 1. Clonar o Repositório
```bash
git clone [https://github.com/RogerioHenrique1403/Keylogger.git](https://github.com/RogerioHenrique1403/Keylogger.git)
cd Keylogger



2. Instalar as Dependências
Recomenda-se a utilização de um ambiente virtual (venv):

# Criar e ativar ambiente virtual (Opcional)
python -m venv venv
source venv/bin/activate  # No Linux/Mac
# venv\\Scripts\\activate  # No Windows

# Instalar biblioteca necessária
pip install pynput



3. Executar o Script
python keylogger.py



Nota: Dependendo do sistema operativo (especialmente em macOS/Linux), poderá ser necessário executar o script com privilégios de administrador (sudo) ou conceder permissões de Acessibilidade nas definições do sistema.

🛡️ Como se Proteger contra Keyloggers?
O estudo de caso deste malware simples serve para compreender a importância das seguintes medidas defensivas:

Antivírus e EDR: Utilizar soluções de segurança atualizadas que consigam detetar assinaturas de scripts ou comportamentos suspeitos (como a monitorização global de inputs).

Princípio do Menor Privilégio: Nunca executar programas desconhecidos como Administrador (root/sudo).

Autenticação de Dois Fatores (2FA): Minimiza o impacto caso as suas credenciais sejam capturadas, pois o código temporário expira rapidamente.

Teclados Virtuais: Utilizados frequentemente por instituições bancárias para introduzir passwords críticas sem usar o teclado físico.