# ELARA — prévia pública

Prévia para avaliação da cliente, com seletor entre vermelho e degradê. A versão em degradê pode ser aberta com `?paleta=degrade`.

Este repositório contém apenas os arquivos públicos prontos para o navegador em `site/` e a configuração de publicação. O código-fonte de desenvolvimento e seu histórico permanecem privados.

O conteúdo é uma demonstração, com `noindex`; não configura checkout nem atendimento por WhatsApp. Não é a publicação final de vendas.

## Editor visual

`/editor/` oferece a camada original Inline Editor 1.6.1 sobre a mesma LP, também com `?paleta=degrade`. O HTML de autoria é autocontido e carrega aproximadamente 10,16 MB; a landing normal não carrega o editor. **Salvar editável** e **Exportar final** baixam arquivos locais e não modificam o site publicado. Uma nova publicação exige revisão e release. No editor, Layout → Tamanho permite dimensões numéricas e alças para imagens e CTAs.

## Publicação rastreável

Cada entrega é revisada por Pull Request antes de integrar `main`. O workflow manual recebe uma tag anotada `preview-*` e seu SHA completo, verifica os hashes do manifesto e publica exclusivamente `site/` no Pages. Não existe publicação automática ao fazer push.

O arquivo público `build.json` identifica o commit fonte do conteúdo e os hashes dos arquivos. As tags e o histórico deste repositório identificam o pacote publicado. O primeiro deploy não possui release anterior de rollback; os seguintes devem preservar a tag anterior.
Prévia pública da ELARA para avaliação da cliente. Somente arquivos estáticos prontos para o navegador.
