# Ryan Victor Test
# Leitor de arquivos CSV que aponta erros nos campos, de acordo com um padrão

## instalação

- certifique-se de que tenha o [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) instalado no seu computador
- certifique-se de que tenha o [python3](https://www.python.org/downloads/) instalado em seu computador
- navegue até um diretorio de sua preferência, abra um terminal e digite:
- `git clone link-so-seu-projeto`
- Ou se preferir, basta clicar [aqui](https://www.youtube.com/watch?v=sCtsJNB2YGg) para baixar o zip do programa.
- Se quiser efetuar os testes, basta dar um `pip install requirements.txt` na raiz do projeto
  (ou Apenas rodar o comando `pip install pytest`)

---

## Modo de uso:
Com o projeto clonado, e as depêndencias instaladas devidamente:
### no terminal:
- 1- Abra um terminal na raiz do programa e execute o seguinte comando:
- `python3 core/__main__.py`
#### 2- copie um arquivo CSV no identado como no teste, e cole no terminal.
- (Basta clicar no arquivo com o botao direito e copiar no linux)
- Ou selecione o "full path" do arquivo e cole no terminal, também funciona.
- Dê um enter.
- Os erros serão exibidos na tela, conforme foi requerido no teste.
- #### PS: um teste, irá falhar, pois tem que colar o path absoluto do arquivo nele, pois não usei nenhuma biblioteca. `(csv_reader_test.py` (linha 1)) 
- fazendo isso, todos os testes irão passar.

### Na IDE (Recomendo o pycharm):
- 1- Basta colar um arquivo .csv dentro da pasta `core`

### importante:
- ##### 2- substituir o nome do arquivo na linha 8 pelo nome do arquivo que foi colado la (entre aspas simples)
- 3- dentro do arquivo `__main__.py`, rodar o programa.
- (4) -Para a execução dos testes, basta rodar um por um rodando cada arquivo, ou digitar `pytest` na raiz do projeto, pelo terminal da IDE