# Registro da release preview-2026.10.22.2

## Fonte e homologação

- Issue47/branchfeat/47-support-pages: base09d968bac65d69ac519619d5839ed209d89b00ac, sincronizada com82d99cc8529d1fd6823aef5fb46b451e7c052f23 pelo merge111bd7acfbf6a12d00ae15c3c8d1953bccef9c51; headc6a79a57b8872184e9832bc58349f1a6773e5cd5; PR48 merge882ad357aec142d54a89ab167a57234c2316b7d3.
- Issue49/branchfix/49-presencial-photo-deadline: base882ad357aec142d54a89ab167a57234c2316b7d3, headdaa2e4c815e243cb72be9e4ea689f5dd4e170c23; PR50 merge4c6baf025d1bb8782568ea3d1252b5eb7c3868b1.
- Issue51/branchfix/51-checkout-link: base4c6baf025d1bb8782568ea3d1252b5eb7c3868b1, head40cd93cc83659451e845e55d0708fadecf687019; PR52 merge finalf7e3c2fffda72a7d1dc782bbc84297d74304740f.
- Todos os PRs da fonte mergeados no GitHub após autorização do usuário e revisão; main sincronizada por fast-forward, branches preservadas, nenhuma exclusão/force-push. Tag anotada da fontepreview-2026.10.22.2 no SHA final.
- Issue pública29, branchrelease/29-support-pages baseada emc9a703e470ee4a2fb4933e5b63cd8c9e471e21b0; SHA do pacote/merge/tag serão identificados pelo PR e release públicos.

## Preflight e testes

Fonte limpa: build-1792691548527,319 recursos,40.135.685bytes; build/check/diff aprovados. Páginas de suporte4/4 casos passaram após sincronização, acessibilidade AA nas duas páginas em320/390/768/1440, URLs profundas, GET/HEAD404, recursos, teclado/sem JS. Foto original do grupo com tratamento CSS e recorte aprovado em320/390/768/1440/1920; tentativa generativa descartada por alterar rostos.3 casos dirigidos de prazo/valores/presenciais e3 de checkout/toque interceptado/prazo aprovados. Audit completo0 vulnerabilidades, lockfile sem mudanças. Suíte completa histórica não repetida: escopo focado e testes dirigidos registrados.

Pacote público:650 recursos íntegros; home/comparação equivalentes salvo módulo de entrada#prova; suporte e prazo/checkout conferidos pelo verificador do workflow. QA local8/8 registros:home/comparação390/1440, seis CTAs novos, prazo24/11, imagem/cor/recorte, seletores8/14/7, sem overflow/erros/404 de recursos; obrigada/404 estáticas sem JS, URLs profundas/status reais e retorno à home. Evidência JSON ao lado.

Ambiente GitHub Pages: https://selvalabs.github.io/elara-preview/, site/ e site/porqueelaraimg/. Permissões Pages/OIDC existentes, nenhum segredo no cliente; configuração/recursos disponíveis. Disco local18,4GB disponível; publicação estática sem serviço/VPS a reiniciar. Nenhum dado/banco/migração/Docker/mirror. Checkout Kiwify externo não foi configurado; apenas os destinos da LP foram atualizados paraM5pqPmr.

## Deploy, pós-verificação e rollback

Somente após merge público: tag anotadapreview-2026.10.22.2 no SHA exato e workflow manual com tag/SHA. Conferir jobssuccess, manifests/SHAs/hashes, quatro páginas, status404 real em URL profunda, CTAs/foto/prazo e home/comparação no navegador público. Registrar resultado na release pública. Rollback: mesmo workflow com preview-2026.10.22.1/c9a703e470ee4a2fb4933e5b63cd8c9e471e21b0, preservado. Sem migração limitando reversão.
