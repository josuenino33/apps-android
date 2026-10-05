# 📱 Apps Android

Instaladores Android (APK) dos meus apps. Baixe, instale e use como qualquer outro app do celular, sem Play Store.

| App | O que é | Baixar |
|---|---|---|
| 🥁 **Bateria** | Bateria do zero ao pro: 292 exercícios, partitura que toca, metrônomo e professor que ouve seu tempo | [bateria-do-zero-ao-pro.apk](https://github.com/josuenino33/apps-android/releases/latest/download/bateria-do-zero-ao-pro.apk) |
| 🎸 **Guitarra** | Guitarra do zero ao pro: 79 aulas, mapa do braço interativo, acordes e licks | [guitarra-do-zero-ao-pro.apk](https://github.com/josuenino33/apps-android/releases/latest/download/guitarra-do-zero-ao-pro.apk) |
| 💪 **Treino** | Treino em casa do zero: 7 trilhas e 55 níveis com o peso do corpo | [treino-em-casa-do-zero.apk](https://github.com/josuenino33/apps-android/releases/latest/download/treino-em-casa-do-zero.apk) |
| 🎤 **Canto** | Canto do zero ao pro: 311 exercícios, piano que guia no seu tom e professor que ouve a sua afinação | [canto-do-zero-ao-pro.apk](https://github.com/josuenino33/apps-android/releases/latest/download/canto-do-zero-ao-pro.apk) |

Todas as versões ficam em [Releases](https://github.com/josuenino33/apps-android/releases).

## Como instalar

1. Abra o link do app **no celular** e baixe o arquivo `.apk`.
2. Toque no arquivo baixado. Na primeira vez, o Android pede para permitir instalar apps do navegador ou do gerenciador de arquivos: permita.
3. Toque em **Instalar** e depois em **Abrir**.

O app aparece na lista de apps, abre em tela cheia, tem tela de abertura própria e desinstala como qualquer outro.

## Como funciona

Cada APK é uma [Trusted Web Activity](https://developer.chrome.com/docs/android/trusted-web-activity): um app Android que abre o site do app em tela cheia usando o motor do Chrome.

- **Atualizações:** o conteúdo vem do site no GitHub Pages. Quando um app é atualizado no repositório dele, o APK já abre a versão nova, sem precisar instalar de novo.
- **Dados:** ficam no celular, os mesmos de quem usa pelo Chrome.
- **Microfone, sem internet, tela ligada:** funcionam como no site.
- **Tela cheia:** o arquivo [assetlinks.json](https://josuenino33.github.io/.well-known/assetlinks.json), publicado no repositório [josuenino33.github.io](https://github.com/josuenino33/josuenino33.github.io), prova para o Android que o app e o site são do mesmo dono. Sem ele, apareceria uma barra de endereço no topo.
- Se o celular não tiver um navegador compatível, o app abre numa visualização interna (WebView).

## Gerar uma versão nova do APK

Só é preciso quando mudar algo do próprio app Android (nome, ícone, cores ou endereço). Mudanças no conteúdo dos sites não exigem APK novo.

1. Aba **Actions** → **Gerar APKs** → **Run workflow**.
2. Informe o número da versão (por exemplo `1.0.1`) e confirme.
3. Em uns 5 minutos a versão aparece em **Releases**, com os quatro APKs.

Os ícones são gerados a partir dos ícones dos sites com `python tools/make_icons.py` (precisa de Pillow).

## Chave de assinatura

Os APKs são assinados com uma chave guardada fora do repositório, nos segredos do GitHub (`KEYSTORE_BASE64` e `KEYSTORE_PASSWORD`), com uma cópia no computador do autor. O Android só aceita atualizar um app se a versão nova vier com a mesma chave, então ela nunca deve ser trocada nem perdida.

## Estrutura

```
app/build.gradle             os quatro apps (flavors): nome, endereço, cores e id de cada um
app/src/main/AndroidManifest.xml   configuração da Trusted Web Activity
app/src/<app>/res/           ícones e tela de abertura de cada app
.github/workflows/apk.yml    monta, assina e publica os APKs
tools/make_icons.py          gera os ícones a partir dos sites
```
