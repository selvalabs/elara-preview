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


## Release preview-2026.10.22.1

Fonte homologada: 82d99cc8529d1fd6823aef5fb46b451e7c052f23 (selvalabs/elara-lp#46, issue45; base09d968bac65d69ac519619d5839ed209d89b00ac; branchfix/45-client-copy; head792f2c095fd86456febd1fdbe20c942693a5a544). Publicação pela issue27 na branchrelease/27-porqueelaraimg, baseada em afcf2e7ddbc5cd91e609b6a2322161f3f6144470.

A home e /porqueelaraimg/ usam o mesmo build completo e todos os ajustes homologados: headline/apoio, Caminho do Feminino, bônus individual limitado às10 primeiras inscritas, fechamento do WhatsApp em duas linhas, notebook4:3 com quatro capturas e depoimentos por navegação manual. Os três cards mantêm as imagens anteriores e incluem as novas opções tratadas, com8/14/7 opções independentes por clique e teclado, sem instrução visível ou autoplay. A home inicia no hero; /porqueelaraimg/ inicia em #prova, respeitando o cabeçalho e sem impedir a navegação posterior. Nenhuma ferramenta de autoria é carregada nessas duas páginas.

Validação da fonte: build/check aprovados, npm audit0 vulnerabilidades. Suíte completa46 casos:41 aprovados inicialmente; cinco falhas corrigidas e os cinco casos repetidos/aprovados. QA dirigido dos seletores em360/390/768/1440. Pacote com manifestos/hashes, equivalência de HTML entre rotas e validação de caminho de entrada. Recursos antigos versionados permanecem no manifesto para não excluir histórico local. Scripts de empacotamento/verificação em scripts/.

Ambiente: GitHub Pages, preview com noindex, sem banco/migrações/VPS/mirror. Deploy manual somente da tag anotada e SHA imutável após merge. Verificação posterior: build.json das duas rotas, links/recursos HTTP200, abertura e seleção de imagens em mobile/desktop. Rollback: redeploy da tag preview-2026.10.21.3 / afcf2e7ddbc5cd91e609b6a2322161f3f6144470, preservada.

QA do pacote:8 combinações aprovadas (390/1440, home/comparação, movimento normal/reduzido), ciclos8/14/7 e teclado, fallback sem JS, reload da comparação e rolagem posterior, links legais HTTP200, sem overflow/erros JS/recursos404. Evidência:verification/preview-2026.10.22.1-qa.json. Disco local disponível no preflight:19,1GB. Configuração comercial e recursos locais preservados; nenhuma variável secreta necessária para o site estático. Deploy usa permissões Pages/OIDC do workflow existente.


## Release preview-2026.10.22.2

Fonte final homologadaf7e3c2fffda72a7d1dc782bbc84297d74304740f reúne:PR48/issue47 (obrigada e404), PR50/issue49 (foto presencial e prazo24/11), PR52/issue51 (checkoutM5pqPmr). Bases/heads/merges registrados no relatório desta release. Branch públicarelease/29-support-pages, issue29, basec9a703e470ee4a2fb4933e5b63cd8c9e471e21b0.

Home e /porqueelaraimg/ completas com todos os ajustes anteriores preservados; comparação inicia em#prova e mantém seletores8/14/7. Obrigada orienta confirmação por e-mail/acesso à MemberKit oficial/WhatsApp sem atestar transação pela visita. 404 da raiz do Pages preserva status404 e caminhos de recursos/retorno em URLs profundas. Sem JavaScript/coleta nas páginas de suporte. Nenhuma configuração de redirecionamento da Kiwify foi alterada.

Foto real enviada do grupo no card Encontros presenciais opcionais, original com tratamento CSS para preservar rostos, recorte responsivo e sem zoom no hover. Prazo Black Rose até24/11/2026 às23h59Brasília, contador e fallback. Seis links de compra atualizados para https://pay.kiwify.com.br/M5pqPmr; preços/WhatsApp/copy preservados.

Validação fonte:build/check/diff; testes de suporte4/4 em320/390/768/1440, GET/HEAD404 e URLs profundas, sem JS/teclado/AA sem violações; foto320/390/768/1440/1920 com capturas inspecionadas;3 testes de contador/oferta/presenciais e3 testes de checkout/toque interceptado/prazo aprovados. Audit completo0 vulnerabilidades; lockfile inalterado. Suíte histórica completa não repetida para alterações focadas, cobertas por conjuntos dirigidos e QA do pacote.

Ambiente GitHub Pages, preview com noindex, site/ e site/porqueelaraimg/. Nenhum banco/migração/VPS/mirror. Checkout fonte e pacote limpos no SHA aprovado; tag anotada antes do deploy manual com SHA/tag exatos. Configuração comercial e recursos locais disponíveis, Pages/OIDC existente, nenhum segredo no cliente. Rollback:preview-2026.10.22.1/c9a703e470ee4a2fb4933e5b63cd8c9e471e21b0 preservado. Nenhuma exclusão.

QA final do pacote:8/8 registros aprovados; fonte final limpa319 recursos, pacote650 recursos íntegros. Relatório/identidades e evidência em verification/preview-2026.10.22.2-report.md e verification/preview-2026.10.22.2-qa.json. Pós-deploy será registrado na release pública.
