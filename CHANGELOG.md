# Changelog

## 0.15.0 (2025-01-11)

Full Changelog: [v0.14.0...v0.15.0](https://github.com/groq/groq-python/compare/v0.14.0...v0.15.0)

### Features

* **api:** api update ([#175](https://github.com/groq/groq-python/issues/175)) ([61cffbc](https://github.com/groq/groq-python/commit/61cffbc78a279fd4ac04d338690925c4f19fa20a))


### Bug Fixes

* correctly handle deserialising `cls` fields ([#174](https://github.com/groq/groq-python/issues/174)) ([0b2e997](https://github.com/groq/groq-python/commit/0b2e997ce4dfad51b7d4d87c5fa5d376488b4d04))


### Chores

* **internal:** codegen related update ([#172](https://github.com/groq/groq-python/issues/172)) ([d6ecada](https://github.com/groq/groq-python/commit/d6ecadaa2433245acaa21bee0ea003e69a9bcb0a))

## 0.14.0 (2025-01-09)

Full Changelog: [v0.13.1...v0.14.0](https://github.com/groq/groq-python/compare/v0.13.1...v0.14.0)

### Features

* **api:** api update ([#163](https://github.com/groq/groq-python/issues/163)) ([43a7a5b](https://github.com/groq/groq-python/commit/43a7a5b048b22f4a5edba53ec31b2b8967681708))
* **api:** api update ([#167](https://github.com/groq/groq-python/issues/167)) ([5016206](https://github.com/groq/groq-python/commit/5016206e461c384806ac3c68b8dfab3d342ba93c))
* **api:** api update ([#170](https://github.com/groq/groq-python/issues/170)) ([2b35e95](https://github.com/groq/groq-python/commit/2b35e952e12020116adc45e40007c3fd61db1bb7))


### Bug Fixes

* **client:** only call .close() when needed ([#169](https://github.com/groq/groq-python/issues/169)) ([6a0ec57](https://github.com/groq/groq-python/commit/6a0ec576de707ed90a4a536ff206e9ee07fc5a3a))


### Chores

* add missing isclass check ([#166](https://github.com/groq/groq-python/issues/166)) ([9cb1e72](https://github.com/groq/groq-python/commit/9cb1e727377c93c92d1bbd49f1c5b8613730c3a6))
* **internal:** bump httpx dependency ([#168](https://github.com/groq/groq-python/issues/168)) ([c260ae9](https://github.com/groq/groq-python/commit/c260ae969caa5f4e7b48dd558802b933da98bed6))
* **internal:** codegen related update ([#158](https://github.com/groq/groq-python/issues/158)) ([85b5765](https://github.com/groq/groq-python/commit/85b5765b2b6cfa9560c763600699fd05f7b2a632))
* **internal:** codegen related update ([#160](https://github.com/groq/groq-python/issues/160)) ([8b87c4d](https://github.com/groq/groq-python/commit/8b87c4d657e0a9d2296323eff6d298ec98b34b3e))
* **internal:** codegen related update ([#164](https://github.com/groq/groq-python/issues/164)) ([d7b6be5](https://github.com/groq/groq-python/commit/d7b6be5f4bba87002409330644045ba630856880))
* **internal:** fix some typos ([#162](https://github.com/groq/groq-python/issues/162)) ([32482ae](https://github.com/groq/groq-python/commit/32482ae691f24fdbd5c80282c597a299a48a247d))


### Documentation

* **readme:** example snippet for client context manager ([#161](https://github.com/groq/groq-python/issues/161)) ([b7bfd15](https://github.com/groq/groq-python/commit/b7bfd15768d60beb2059ab3d326bae1b19c6bf17))

## 0.13.1 (2024-12-14)

Full Changelog: [v0.13.0...v0.13.1](https://github.com/groq/groq-python/compare/v0.13.0...v0.13.1)

### Chores

* **internal:** add support for TypeAliasType ([#153](https://github.com/groq/groq-python/issues/153)) ([c5ca4fc](https://github.com/groq/groq-python/commit/c5ca4fc7c1ced7e49f06d05e67924f702e5e021d))
* **internal:** bump pydantic dependency ([#150](https://github.com/groq/groq-python/issues/150)) ([63e5754](https://github.com/groq/groq-python/commit/63e5754857bcbc137350971520cf9997e4d78da3))
* **internal:** bump pyright ([#145](https://github.com/groq/groq-python/issues/145)) ([8f2b3a0](https://github.com/groq/groq-python/commit/8f2b3a0d70dad49b652a61f549979c1c5125d9d4))
* **internal:** bump pyright ([#152](https://github.com/groq/groq-python/issues/152)) ([75476cd](https://github.com/groq/groq-python/commit/75476cd26c33e48220ab8760e129cd3f70413df5))
* **internal:** codegen related update ([#154](https://github.com/groq/groq-python/issues/154)) ([db44bd6](https://github.com/groq/groq-python/commit/db44bd6adfb1eddfee9ee06cc63d4c594713eebc))
* **internal:** codegen related update ([#155](https://github.com/groq/groq-python/issues/155)) ([7f303c3](https://github.com/groq/groq-python/commit/7f303c31dbebfe97b97388ff7f29238fc917da43))
* **internal:** updated imports ([#156](https://github.com/groq/groq-python/issues/156)) ([3f41c12](https://github.com/groq/groq-python/commit/3f41c12bd36e13eba37d2bd7fd4f3f595bda4602))
* make the `Omit` type public ([#147](https://github.com/groq/groq-python/issues/147)) ([0613ae1](https://github.com/groq/groq-python/commit/0613ae1e9f9dede7cb951d2d0591017894576b3a))


### Documentation

* **readme:** fix http client proxies example ([#151](https://github.com/groq/groq-python/issues/151)) ([b858c4f](https://github.com/groq/groq-python/commit/b858c4f742bdd7aae79f17981cb9d3b001ed009b))

## 0.13.0 (2024-11-28)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/groq/groq-python/compare/v0.12.0...v0.13.0)

### Features

* **api:** api update ([#134](https://github.com/groq/groq-python/issues/134)) ([fde3a90](https://github.com/groq/groq-python/commit/fde3a90bf0d3d37dc46765198445becaf588ee96))


### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#142](https://github.com/groq/groq-python/issues/142)) ([b8abf89](https://github.com/groq/groq-python/commit/b8abf8961949a9698c7eb666562acbaab15ce9ea))


### Chores

* **internal:** exclude mypy from running on tests ([#141](https://github.com/groq/groq-python/issues/141)) ([fb4456e](https://github.com/groq/groq-python/commit/fb4456e36a6630a3a07e9f1fec09ae335b0554d7))
* **internal:** fix compat model_dump method when warnings are passed ([#138](https://github.com/groq/groq-python/issues/138)) ([91402fd](https://github.com/groq/groq-python/commit/91402fd2ac19b0be2ec1b360e541c891cb4d651f))
* rebuild project due to codegen change ([#136](https://github.com/groq/groq-python/issues/136)) ([b79c1f9](https://github.com/groq/groq-python/commit/b79c1f96496074cc38c489f4b79fa63b871354b7))
* rebuild project due to codegen change ([#137](https://github.com/groq/groq-python/issues/137)) ([2899a88](https://github.com/groq/groq-python/commit/2899a88502cb48aaf99fdc3a277c925ec1137583))
* remove now unused `cached-property` dep ([#140](https://github.com/groq/groq-python/issues/140)) ([d001e95](https://github.com/groq/groq-python/commit/d001e95f7d3f8882eb741c87f66422ef6343260f))


### Documentation

* add info log level to readme ([#139](https://github.com/groq/groq-python/issues/139)) ([804a891](https://github.com/groq/groq-python/commit/804a8910914001d9e21cff974b281011979352f3))

## 0.12.0 (2024-11-12)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/groq/groq-python/compare/v0.11.0...v0.12.0)

### Features

* **api:** api update ([#127](https://github.com/groq/groq-python/issues/127)) ([2f20c22](https://github.com/groq/groq-python/commit/2f20c227860ec41c9255b5b7dd7d0af2dd98c7f9))
* **api:** api update ([#129](https://github.com/groq/groq-python/issues/129)) ([41c4f28](https://github.com/groq/groq-python/commit/41c4f280afb004f41994d8456d63f21acd6da6a9))


### Bug Fixes

* GitHub Terraform: Create/Update .github/workflows/stale.yaml [skip ci] ([537cc49](https://github.com/groq/groq-python/commit/537cc4977b4fcc1c7679abcc9ca4ddf2fbafdcd2))


### Chores

* rebuild project due to codegen change ([#130](https://github.com/groq/groq-python/issues/130)) ([e08a00f](https://github.com/groq/groq-python/commit/e08a00f13f68b8041293f02064d7b6d692a07cd9))
* rebuild project due to codegen change ([#131](https://github.com/groq/groq-python/issues/131)) ([8a3c31d](https://github.com/groq/groq-python/commit/8a3c31d2aa3cb855e6f1feef169be48447adca61))
* rebuild project due to codegen change ([#132](https://github.com/groq/groq-python/issues/132)) ([8287ed4](https://github.com/groq/groq-python/commit/8287ed44c4a668484f4cfc068b86a2132ab19714))

## 0.11.0 (2024-09-03)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/groq/groq-python/compare/v0.10.0...v0.11.0)

### Features

* **internal:** handle streaming error ([#119](https://github.com/groq/groq-python/issues/119)) ([3722579](https://github.com/groq/groq-python/commit/372257924bece8f8d1ffabe866af9d3eafbc6193))

## 0.10.0 (2024-08-27)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/groq/groq-python/compare/v0.9.0...v0.10.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#102](https://github.com/groq/groq-python/issues/102)) ([42a8621](https://github.com/groq/groq-python/commit/42a8621a8ca6fe2656ad449eb84c65dc86c2a119))
* **api:** OpenAPI spec update via Stainless API ([#111](https://github.com/groq/groq-python/issues/111)) ([d860183](https://github.com/groq/groq-python/commit/d860183dae060f32c835179c4754386cb9543e76))
* **api:** OpenAPI spec update via Stainless API ([#115](https://github.com/groq/groq-python/issues/115)) ([007affd](https://github.com/groq/groq-python/commit/007affd05241ff20e3c18c3523015c7a236dc9dd))
* **api:** OpenAPI spec update via Stainless API ([#98](https://github.com/groq/groq-python/issues/98)) ([c3c42ec](https://github.com/groq/groq-python/commit/c3c42ec4cb928a9e1093b8bd4f4232119f73d45c))
* **api:** update via SDK Studio ([#94](https://github.com/groq/groq-python/issues/94)) ([2808c19](https://github.com/groq/groq-python/commit/2808c19d5729978ab6c4093b69cd9845cc75907e))
* **api:** update via SDK Studio ([#97](https://github.com/groq/groq-python/issues/97)) ([97f8a0a](https://github.com/groq/groq-python/commit/97f8a0a2397deecd9134075a7fb44100b7c51611))


### Chores

* **ci:** limit release doctor target branches ([#105](https://github.com/groq/groq-python/issues/105)) ([629f2d0](https://github.com/groq/groq-python/commit/629f2d02ac844bcfeee0df9025df657d5950345c))
* **docs:** document how to do per-request http client customization ([#104](https://github.com/groq/groq-python/issues/104)) ([9334f8b](https://github.com/groq/groq-python/commit/9334f8bf89f9686263f150f94b83465045a73a53))
* **internal:** codegen related update ([#103](https://github.com/groq/groq-python/issues/103)) ([7f92641](https://github.com/groq/groq-python/commit/7f92641ae9513913ab82eb1d36b799518c814238))
* **internal:** codegen related update ([#112](https://github.com/groq/groq-python/issues/112)) ([4a94475](https://github.com/groq/groq-python/commit/4a94475d449f04882c06007798319fb1a23b5079))
* **internal:** codegen related update ([#117](https://github.com/groq/groq-python/issues/117)) ([e4bc523](https://github.com/groq/groq-python/commit/e4bc52371263db69f1d2f37ea651c7400ca1f8f3))
* **internal:** use different 32bit detection method ([#113](https://github.com/groq/groq-python/issues/113)) ([b7f33d6](https://github.com/groq/groq-python/commit/b7f33d6e22537b57f5bc155260ca10af0a0eeaec))
* **tests:** update prism version ([#106](https://github.com/groq/groq-python/issues/106)) ([360ba04](https://github.com/groq/groq-python/commit/360ba0402f65e1579fc15a93b8f1b7254ee28a00))

## 0.9.0 (2024-06-11)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/groq/groq-python/compare/v0.8.0...v0.9.0)

### Features

* **api:** Fix audio transcription response formats ([88e3d61](https://github.com/groq/groq-python/commit/88e3d61ca46949ff32c14a39416e0d7278d80997))
* **api:** Tool calling features ([c081730](https://github.com/groq/groq-python/commit/c0817302fb83b4a4f61397f79d51c214280a77ae))

## 0.8.0 (2024-05-22)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/groq/groq-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** Define OpenAI-compatible models ([bc1bb7b](https://github.com/groq/groq-python/commit/bc1bb7b272ff424ec8eeb2b488a30940263c8fa5))


### Chores

* fix array indices in README examples ([5056621](https://github.com/groq/groq-python/commit/505662127635c4a3d77b57a8bbb3a8361227a02f))
* patch streaming ([9dcba61](https://github.com/groq/groq-python/commit/9dcba614f7a41975df4e0486b6b497653a482dbc))

## 0.5.0 (2024-04-11)

Full Changelog: [v0.4.2...v0.5.0](https://github.com/groq/groq-python/compare/v0.4.2...v0.5.0)

### Features

* Add transcription and translation endpoints ([d6be6e7](https://github.com/groq/groq-python/commit/d6be6e7fe0946c107b135bf629190041f241394b))


### Chores

* add CODEOWNERS ([a1594a7](https://github.com/groq/groq-python/commit/a1594a7e462c2e7a0deb8e32b17adf6f81d55ef1))
* **examples:** lint ([fdcb94e](https://github.com/groq/groq-python/commit/fdcb94ee77b05fbcb926a3b80f5016626d202637))
* Fix streaming before release ([7dec9b7](https://github.com/groq/groq-python/commit/7dec9b711c222dec4f4a86d7e6c650525066d2aa))

## 0.4.2 (2024-03-01)

Full Changelog: [v0.4.1...v0.4.2](https://github.com/groq/groq-python/compare/v0.4.1...v0.4.2)

### Features

* OpenAPI spec update via Stainless API ([#19](https://github.com/groq/groq-python/issues/19)) ([84ad1a4](https://github.com/groq/groq-python/commit/84ad1a4cd90eeee21a8f7bed1003ea8c51669f29))

## 0.4.1 (2024-02-21)

Full Changelog: [v0.1.0...v0.4.1](https://github.com/groq/groq-python/compare/v0.1.0...v0.4.1)

### Features

* Add initial Stainless SDK ([4de80db](https://github.com/groq/groq-python/commit/4de80dbe4c27d6ecbcc2d2b6192d27ade5da3866))
* Add initial Stainless SDK ([d5a8512](https://github.com/groq/groq-python/commit/d5a851262e04e625dde130367ed91d8f95683599))
* Add initial Stainless SDK ([316de2c](https://github.com/groq/groq-python/commit/316de2ccfeb76e36fe34bb8656ea90a8d42a7d00))
* create default branch ([7e00266](https://github.com/groq/groq-python/commit/7e00266e3c691d92d508e753e2c14c03297c09f9))
* update via SDK Studio ([#10](https://github.com/groq/groq-python/issues/10)) ([0c0d204](https://github.com/groq/groq-python/commit/0c0d20405a96167f060a03a2b8a58a49d9a1c7c8))
* update via SDK Studio ([#14](https://github.com/groq/groq-python/issues/14)) ([153744e](https://github.com/groq/groq-python/commit/153744e8ca331900adb0bd88a688afedf9a4bf00))
* update via SDK Studio ([#3](https://github.com/groq/groq-python/issues/3)) ([8d92c08](https://github.com/groq/groq-python/commit/8d92c086e320c2715e02bc79807ff872e84c0b0f))


### Chores

* go live ([#2](https://github.com/groq/groq-python/issues/2)) ([ba81c42](https://github.com/groq/groq-python/commit/ba81c42d6d0fd6d47819e0d58962235cb70ca4f1))
* go live ([#5](https://github.com/groq/groq-python/issues/5)) ([75ea081](https://github.com/groq/groq-python/commit/75ea081a84bbcf15702dcb53fd6411c8de497c83))
* go live ([#5](https://github.com/groq/groq-python/issues/5)) ([af9a838](https://github.com/groq/groq-python/commit/af9a838e240bb0f7385bc33fb18ce246427ca2f7))
* update branch ([#12](https://github.com/groq/groq-python/issues/12)) ([28f34e1](https://github.com/groq/groq-python/commit/28f34e1cc08b974d31744fd94bf31eafc9e6e867))
* update branch ([#8](https://github.com/groq/groq-python/issues/8)) ([b9b55b4](https://github.com/groq/groq-python/commit/b9b55b41cb158efd155f9cda829808c877493afd))

## 0.1.0 (2024-02-10)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/definitive-io/groqcloud-python/compare/v0.0.1...v0.1.0)

### Features

* Add initial Stainless SDK ([1c7e467](https://github.com/definitive-io/groqcloud-python/commit/1c7e4677c395264d479a37f0ed896131a08446f9))
* create default branch ([1320cdb](https://github.com/definitive-io/groqcloud-python/commit/1320cdb659ef51e3abbd919306631070d8dd6dcf))
* OpenAPI spec update ([#1](https://github.com/definitive-io/groqcloud-python/issues/1)) ([87e86b0](https://github.com/definitive-io/groqcloud-python/commit/87e86b09c428f65915d377759a4dbba686b2197a))
* OpenAPI spec update ([#3](https://github.com/definitive-io/groqcloud-python/issues/3)) ([90308e1](https://github.com/definitive-io/groqcloud-python/commit/90308e13a706230c32f567820fa92dfa83d89942))
* OpenAPI spec update ([#4](https://github.com/definitive-io/groqcloud-python/issues/4)) ([e983af3](https://github.com/definitive-io/groqcloud-python/commit/e983af307498e4ea87b492ff7f62e1309865746f))
* OpenAPI spec update ([#5](https://github.com/definitive-io/groqcloud-python/issues/5)) ([cfdd6ac](https://github.com/definitive-io/groqcloud-python/commit/cfdd6ac768e5539ecefd8c06df614ce2bdd4dd7e))
