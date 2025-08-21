Vantagens de se usar mensagem de finalização para encerramento da conexão

- Maior controle no encerramento da conexão
- Ambos, clientes e servidor, ficam cientes do encerramento
- Possibilidade de implementar mensagens próprias de encerramento

Desvantagens de se usar mensagem de finalização para encerramento da conexão

- É necessário que cliente e servidor combinem os códigos de encerramento
- Se a conexão cair antes da mensagem de encerramento, teremos problema para
  encerrar a conexão, sem um timeout definido

  Motivos pelos quais meu cliente-servidor não transfere arquivos grandes como deveria

  - send, recv, sendto e recvfrom não garatem o envio ou recebimento de todos os bytes de uma só vez
  - Para arquivos grandes é necessário usar chunk e criar um laço para garantir o recebimento de todos os bytes
  - Buffer limitado