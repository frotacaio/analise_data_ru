# analise_data_ru
Repositório referente ao trabalho final da disciplina de Ciências de Dados. Destina-se à aplicação de análise de dados e criação de modelos de regressão para o Banco de dados do RU.


## Desenvolvimento

### Pré-requisitos
* Python 3.10+
* [Poetry](https://python-poetry.org/docs/)


### Instalação do poetry
* Olhar [documentação](https://python-poetry.org/docs/#installation)


Para instalação no **Windows**:

1. No Powershell executar o comando para instalar o Poetry

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

2. Verificar se o arquivo `poetry.exe` existe:

```powershell
ls $env:APPDATA\Python\Scripts
```

* **Se der erro, tentar instalar de novo.**

3. Salvar path antigo por segurança:

```powershell
$old_path = "$env:path"
```

4. Para adicionar o poetry no Path, basta rodar:

```powershell
[Environment]::SetEnvironmentVariable('PATH', "$env:path;$env:APPDATA\Python\Scripts", 'User')
```

5. Reabrir o powershell e verificar se está instalado:

```powershell
poetry --version
```

### Instalação do projeto
```
poetry install
```
