Algoritmo "Cadastro clientes e destinos, com consulta simples;"
"Aluno Thairony, turma 4"
"encoder preferencial ISO8859-1"

Var
   // Se��o de Declara��es das vari�veis
   clientes:vetor[0..2] de caractere
   destinos:vetor[0..2] de caractere
   cpf:vetor[0..2] de inteiro
   opc: inteiro
   cli:inteiro
   i:inteiro

procedimento cadastraCliente()
                               // cadastra todos os clientes
   inicio
      para i de 0 ate 2 faca
         escreval ("Digite o nome do cliente: ")
         leia (clientes[i])
         escreval ("Digite o destino do cliente: ")
         leia (destinos[i])
         escreval ("Digite o CPF do cliente: ")
         leia (cpf[i])
      fimpara
fimprocedimento


procedimento localizaCliente()
                              // busca cliente da base, pelo CPF
   inicio
      escreval ("Qual cliente deseja localizar?")
      escreva ("Digite o CPF completo [somente n�meros] do cliente:  ")
      leia(cli)
      para i de 0 ate 2 faca
         se cli = cpf[i] entao
            escreval ("Cliente: ", clientes[i])
            escreval ("Destino: ", destinos[i])
            escreval ("CPF: ", cpf[i])
         fimse
      fimpara
fimprocedimento

inicio

   enquanto verdadeiro faca
      escreval ("MENU")
      escreval (" Op��o 1 - Cadastrar clientes: ")
      escreval (" Op��o 2 - localizar cliente: ")
      escreval (" Aperte ESC para SAIR ")
      escreval ()
      Escreva ("root@user:  ")
      leia (opc)
      se opc = 1 entao
         limpatela
         cadastraCliente()

      fimse
      se opc = 2 entao
         limpatela
         localizaCliente()
      fimse
                         // la�o s� se enterrompe junto ao console, com ESC
   fimenquanto

Fimalgoritmo
