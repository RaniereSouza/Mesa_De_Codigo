/**
 * @file Código feito para testar as funcionalidades de leitura e escrita de arquivos de texto em Node.js, bem como implementar um reconhecimento e contagem de palavras via "brute force"
 * 
 * =============================== ContaPalavra.js ===============================
 * 
 * Entradas: 
 *         - o path de um arquivo de texto qualquer codificado em UTF-8;
 *         - um path dizendo qual será o arquivo de saída;
 * 
 * Saídas: 
 *         - um log com um valor numérico, resultante da contagem de palavras;
 *         - um arquivo de texto com as palavras do arquivo de entrada, cada uma
 *           em uma linha;
 * 
 * @author Raniere de Souza Santos <raniere.souza.cc@gmail.com>
 * @version 1.0.0
 */

const fs   = require('fs'), //package padrão do Node.js para acessar o sistema de arquivos do computador
      args = process.argv.slice(2); //recorte dos argumentos da linha de comando, apenas pegando o que foi inserido pelo usuário

//checagem de argumentos vindos da linha de comando
if (!args || (args.length < 2)) { //se não tem os argumentos esperados (os paths dos arquivos de entrada e de saída):
    console.log('not enough arguments to run code');
    process.exit(); //encerra o programa
}

//abrindo streams de leitura (rs = readStream) e escrita (ws = writeStream) dos arquivos de entrada e de saída, respectivamente
var rs = fs.createReadStream(args[0], 'utf8'),
    ws = fs.createWriteStream(args[1], 'utf8');

//handler de erro do stream de leitura (apenas exibe o log do erro)
rs.on('error', (err) => {
    console.log('readStream error:');
    console.log(err.message || err.details || err);
});

//handler de erro do stream de escrita (apenas exibe o log do erro)
ws.on('error', (err) => {
    console.log('writeStream error: ');
    console.log(err.message || err.details || err);
});

//handler para quando o stream de leitura estiver pronto
rs.on('readable', () => {

    let chunk   = rs.read(1), //leitura inicial dos caracteres do arquivo de entrada (parâmetro: número de bytes)
        word    = '', //acumulador de palavra identificada
        regex   = /([a-z]|[0-9]|ã|Ã|á|Á|â|Â|à|À|é|É|ê|Ê|í|Í|õ|Õ|ó|Ó|ô|Ô|ú|Ú|ü|Ü|ç|Ç)/i, //expressão regular de caracteres válidos em uma palavra
        count   = 0, //inicialização do contador de palavras
        rs_done = false, //flag de stream de leitura encerrado
        ws_done = false; //flag de stream de escrita encerrado

    //handler para quando stream de leitura for encerrado (chegou no final do arquivo de entrada)
    rs.on('end', () => {

        if (!rs_done) { //se flag ainda não foi marcada:

            rs_done = true; //evita que handler seja executado duplicadamente

            if (word) count++ && ws.write(word + '\n'); //se ainda houver algo no acumulador de palavra, escrever no arquivo de saída e incrementar a contagem
            ws.end(); //encerrando o stream de escrita
        }
    });

    //handler para quando stream de escrita for encerrado
    ws.on('finish', () => {

        if (!ws_done) { //se flag ainda não foi marcada:

            ws_done = true; //evita que handler seja executado duplicadamente

            console.log(`we found ${count} words!`); //exibindo resultado final da contagem
        }
    });

    //enquanto não atingir o final do arquivo (null), faça:
    while (chunk) {
        
        if (regex.test(chunk)) { //se foi lido um caractere válido:
            word += chunk; //adiciona o caractere no acumulador de palavra
        }
        else if (word) { //se caractere lido não é válido e o acumulador de palavra não está vazio:
            count++; //incremento do contador de palavras
            ws.write(word + '\n'); //escrita de uma palavra por linha no arquivo de saída
            word = ''; //esvaziando o acumulador de palavra
        }

        chunk = rs.read(1); //leitura incremental dos caracteres no arquivo de entrada
    }
});