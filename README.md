# ELARA — prévia pública

Versão aprovada da ELARA com paleta roxinha fixa. A URL principal já abre nessa paleta, sem seletor de cores; links antigos continuam funcionando.

Este repositório contém apenas os arquivos públicos prontos para o navegador em `site/` e a configuração de publicação. O código-fonte de desenvolvimento e seu histórico permanecem privados.

Prévia pública aprovada da campanha Black Rose, com `noindex`. CTAs de compra apontam ao checkout oficial Kiwify; o último CTA após o FAQ abre o WhatsApp oficial. Campanha até 22/11/2026 às 23h59, horário de Brasília. A publicação continua identificada como preview para avaliação da cliente.

## Editor visual

`/editor/` oferece a camada original Inline Editor 1.6.1 sobre a mesma LP, com a paleta roxinha preservada também nas exportações. O HTML de autoria é autocontido e carrega aproximadamente 7,58 MB; a landing normal não carrega o editor. **Salvar editável** e **Exportar final** baixam arquivos locais e não modificam o site publicado. Uma nova publicação exige revisão e release. No editor, Layout → Tamanho permite dimensões numéricas e alças para imagens e CTAs.

## Publicação rastreável

Cada entrega é revisada por Pull Request antes de integrar `main`. O workflow manual recebe uma tag anotada `preview-*` e seu SHA completo, verifica os hashes do manifesto e publica exclusivamente `site/` no Pages. Não existe publicação automática ao fazer push.

O arquivo público `build.json` identifica o commit fonte do conteúdo e os hashes dos arquivos. As tags e o histórico deste repositório identificam o pacote publicado. O primeiro deploy não possui release anterior de rollback; os seguintes devem preservar a tag anterior.
Prévia pública da ELARA para avaliação da cliente. Somente arquivos estáticos prontos para o navegador.

## Ajustes da release preview-2026.10.20.5

Investimento com contorno dourado discreto; encontros presenciais opcionais com inscrição/pagamento à parte; kit com 12 florais de rosas em estojo especial e frete grátis. Dinheiro Feminino: R$ 127; três bônus: R$ 1.421; com o encontro individual de R$ 330: R$ 1.751 em experiências de presente.

O celular apresenta as capas em loop contínuo; o computador alterna quatro capturas/miniaturas reais, incluindo Rosa Arco-Íris e aulas de Psique Feminina. Controles de pausa e avanço, movimento reduzido e fallback sem JavaScript preservados. Os mockups exibem imagens, não vídeos ao vivo.

## Ajustes da release preview-2026.10.20.6

Frame desfavorável retirado do computador: três imagens reais, mantendo Rosa Arco-Íris na abertura. Sustentação com rolagem natural, oito reveals em sequência e risco dourado por último; sem pin. Black Rose sem quebra, quadro dos bônus com contorno suave e WhatsApp no padrão dourado. Copy e dados comerciais preservados.

## Ajustes da release preview-2026.10.21.1

Fonte privada homologada: e53f7b674b614bbf984f553f075a5082f4ae009a (PR #39). Botões responsivos e selos maiores/centralizados; Black Rose separado acima das faixas; relatos com avanço automático e pausa para leitura; rodapé com Termos de Uso e Política de Privacidade, identificação e contato confirmados. Galeria, editor e recursos continuam locais. Sem mudanças de valores, compra ou coleta de dados.

## Release preview-2026.10.21.2

Fonte homologada: 2b6f8f6698ab5fa6df3ec04d60bfe6b5131d3d8d (elara-lp#42). Relatos com pausa por pressão, sem modal/barra e apenas cards completos; WhatsApp fixo; reveals e partículas revisados; notebook mais alto com três capturas fornecidas pelo cliente, recortes e dissolução a cada3s. Pacote estático sem mudanças comerciais ou de dados. Rollback: preview-2026.10.21.1 / 09d33bd07030e0708fff56ef40c78765e9236934.

## Release preview-2026.10.21.3

Fonte homologada: 09d968bac65d69ac519619d5839ed209d89b00ac (elara-lp#44). Reveals de textos e imagens por entrada no viewport, repetidos ao retornar; sustentação reinicia por visita e mantém o risco por último. Títulos centralizados, frase final maior e CTAs sem setas. Botões sem borda interna. Sem mudanças comerciais ou de dados. Rollback: preview-2026.10.21.2 / aed7e636209b5c44bea92bf4030372bbd40c53bf.
