# Changelog

## 0.35.0 (2025-11-18)

Full Changelog: [v0.34.1...v0.35.0](https://github.com/groq/groq-python/compare/v0.34.1...v0.35.0)

### Features

* **api:** api update ([d6ec93d](https://github.com/groq/groq-python/commit/d6ec93d000702baf001b1a5739489d8d5fd7b7da))
* **api:** api update ([48c8f11](https://github.com/groq/groq-python/commit/48c8f11f014207d9665b1eacce3f97461265b12d))


### Bug Fixes

* update chat completion streaming types ([833cf83](https://github.com/groq/groq-python/commit/833cf83b5f2f59eaa17507c330be90a722a871e8))


### Chores

* GitHub Terraform: Create/Update .github/workflows/code-freeze-bypass.yaml [skip ci] ([63d11e3](https://github.com/groq/groq-python/commit/63d11e39fec78e040a95e6e3fe398fe6ca9e1fc2))

## 0.34.1 (2025-11-14)

Full Changelog: [v0.34.0...v0.34.1](https://github.com/groq/groq-python/compare/v0.34.0...v0.34.1)

### Bug Fixes

* Add annotations to streaming response ([#255](https://github.com/groq/groq-python/issues/255)) ([fd2f850](https://github.com/groq/groq-python/commit/fd2f850108029ea08981233235b8ab45aeb88063))

## 0.34.0 (2025-11-12)

Full Changelog: [v0.33.0...v0.34.0](https://github.com/groq/groq-python/compare/v0.33.0...v0.34.0)

### Features

* **api:** api update ([51bb951](https://github.com/groq/groq-python/commit/51bb951f04069bdbc79fbcc96e9a89ad9bb945ed))


### Bug Fixes

* **client:** close streams without requiring full consumption ([99b9431](https://github.com/groq/groq-python/commit/99b9431a9663dc1c2abb8f46c2444fa2bb397eb4))
* compat with Python 3.14 ([edd91d9](https://github.com/groq/groq-python/commit/edd91d90d640b74efcaa7d3085ab387fa069cf58))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([2e981f7](https://github.com/groq/groq-python/commit/2e981f7fdf618c7b85d68a7ba8070bc1e5d3ac37))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([3af43e5](https://github.com/groq/groq-python/commit/3af43e5855668c3632a9053222d11c27fa40c70c))
* **internal:** grammar fix (it's -&gt; its) ([37687bf](https://github.com/groq/groq-python/commit/37687bfc136e87b85f26f9617b02a80e21047858))
* **package:** drop Python 3.8 support ([e45cc65](https://github.com/groq/groq-python/commit/e45cc6572c5da919b903c48c541d6039a188d3ab))

## 0.33.0 (2025-10-21)

Full Changelog: [v0.32.0...v0.33.0](https://github.com/groq/groq-python/compare/v0.32.0...v0.33.0)

### Features

* **api:** api update ([e3ef279](https://github.com/groq/groq-python/commit/e3ef2792b74b312e4242c094071abcfa6d7694a4))
* **api:** api update ([dba73cd](https://github.com/groq/groq-python/commit/dba73cdffede1882bade06dfc84e01c0df984a17))
* **api:** api update ([0008a45](https://github.com/groq/groq-python/commit/0008a452ee15f83d0ac50bb2cff2e7508f5318c1))
* **api:** api update ([b9e85a0](https://github.com/groq/groq-python/commit/b9e85a0362e9597fecad00d42853d38c6ebdd84b))


### Bug Fixes

* bad merge ([1d66042](https://github.com/groq/groq-python/commit/1d6604208a3a0b54f8bc3a32ae24075c7bbc99e8))
* completions overloads ([cf9ad41](https://github.com/groq/groq-python/commit/cf9ad415ec9caa70bb2393c1c31a5de125cbd917))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([f366ae8](https://github.com/groq/groq-python/commit/f366ae888a9a3780f1d5ffacee33b984156a8938))
* do not install brew dependencies in ./scripts/bootstrap by default ([77febdb](https://github.com/groq/groq-python/commit/77febdba2cb98a9731912b35510532ba68c64dfe))
* **internal:** detect missing future annotations with ruff ([b25a9a9](https://github.com/groq/groq-python/commit/b25a9a9f4d42dafa9e82a2336d47dbf8a796fac6))
* **types:** change optional parameter type from NotGiven to Omit ([437d52b](https://github.com/groq/groq-python/commit/437d52b779fc03152b45c7d0a652cab3ea551190))

## 0.32.0 (2025-09-27)

Full Changelog: [v0.31.1...v0.32.0](https://github.com/groq/groq-python/compare/v0.31.1...v0.32.0)

### Features

* **api:** api update ([5d3f1db](https://github.com/groq/groq-python/commit/5d3f1dbe12828c92fcee1c4340e2f1ee9f5764b0))
* **api:** api update ([5b48116](https://github.com/groq/groq-python/commit/5b4811685c7e81cc2933ebc521184fff9c55e267))


### Bug Fixes

* chat stream overloads ([42f9396](https://github.com/groq/groq-python/commit/42f9396959f205f3a439932f1811f82091d0e7f5))
* GitHub Terraform: Create/Update .github/workflows/stale.yaml [skip ci] ([ba00a6e](https://github.com/groq/groq-python/commit/ba00a6e71b7559da44a2d9b2a4babcdfa6d70b85))


### Chores

* **internal:** move mypy configurations to `pyproject.toml` file ([a8113a5](https://github.com/groq/groq-python/commit/a8113a56fc7a57c3c07231fa6925708d038c028f))
* **internal:** update pydantic dependency ([0d8773d](https://github.com/groq/groq-python/commit/0d8773d7520fe91d6eb721b00dbff0dcd850e69c))
* **tests:** simplify `get_platform` test ([a257487](https://github.com/groq/groq-python/commit/a257487327c3601743d49a8d96f74bef4a6c24f7))
* **types:** change optional parameter type from NotGiven to Omit ([882ffc0](https://github.com/groq/groq-python/commit/882ffc0f1f6b1e529b2cd6c3252f75b225fa514a))

## 0.31.1 (2025-09-04)

Full Changelog: [v0.31.0...v0.31.1](https://github.com/groq/groq-python/compare/v0.31.0...v0.31.1)

### Features

* **api:** api update ([0a8a5c0](https://github.com/groq/groq-python/commit/0a8a5c0be7709857fdff72d03a34dce723f13b71))
* **api:** api update ([7896dbd](https://github.com/groq/groq-python/commit/7896dbd7b60828795d2e9780cdf326b001fc839c))
* **api:** api update ([f9b5dca](https://github.com/groq/groq-python/commit/f9b5dca378b9916ca2ab592922b9ffba7247a1ae))
* **api:** api update ([e34ec28](https://github.com/groq/groq-python/commit/e34ec28c9705485684293cfb97eec63b16257bd7))
* **api:** api update ([cd14d0a](https://github.com/groq/groq-python/commit/cd14d0ab7eb0b161ffeef69a7b89cce062aeb078))
* **api:** api update ([7d02cd3](https://github.com/groq/groq-python/commit/7d02cd32852d47016cf3b6cc7ca0f898dd0c99c5))
* **api:** api update ([437f5fb](https://github.com/groq/groq-python/commit/437f5fb2040d345614ffe9ff15c525feb2ab19de))
* improve future compat with pydantic v3 ([42a6cb9](https://github.com/groq/groq-python/commit/42a6cb96e631ad48c371a1ab58b6adea07897685))
* **types:** replace List[str] with SequenceNotStr in params ([d1ee744](https://github.com/groq/groq-python/commit/d1ee74483e6d2e2353985d760837e72af3143be8))


### Bug Fixes

* avoid newer type syntax ([21f93a7](https://github.com/groq/groq-python/commit/21f93a72c50f49187e09310df41e5dbb984298c3))
* compeltions streaming overloads ([201e137](https://github.com/groq/groq-python/commit/201e137d9b336b4fef847713e6e743ac47e733be))
* update example model from decommissioned models to gpt-oss-20b ([1570583](https://github.com/groq/groq-python/commit/1570583818c7355c1ea6cc4460075f60d3cd29bb))
* update example model from decommissioned models to gpt-oss-20b ([#250](https://github.com/groq/groq-python/issues/250)) ([edb9132](https://github.com/groq/groq-python/commit/edb91324ebff8d10f993492dd68ed05ac030bc9f))


### Chores

* **internal:** add Sequence related utils ([01104d8](https://github.com/groq/groq-python/commit/01104d8c4a179a2ad347d0e12f935d6547f61b31))
* **internal:** change ci workflow machines ([e796cb9](https://github.com/groq/groq-python/commit/e796cb9599db99fa9e29f97e54ffe519bd23bf1b))
* **internal:** fix ruff target version ([b58149d](https://github.com/groq/groq-python/commit/b58149d9584a5c9b0afc935af6aef2a2c64c1187))
* **internal:** update comment in script ([bd20c49](https://github.com/groq/groq-python/commit/bd20c49c957e990aeb8c3bb8bb9c3dc9bcc31b86))
* **internal:** update pyright exclude list ([124e838](https://github.com/groq/groq-python/commit/124e8387b8ba18853f93dede16ffba8c49c441a0))
* update @stainless-api/prism-cli to v5.15.0 ([b2f49cc](https://github.com/groq/groq-python/commit/b2f49cc1301696827eb00d5db91895d71c3da965))
* update github action ([c7662e0](https://github.com/groq/groq-python/commit/c7662e01641af2daa758eb23bb19c9b65d0d5d20))

## 0.31.0 (2025-08-05)

Full Changelog: [v0.30.0...v0.31.0](https://github.com/groq/groq-python/compare/v0.30.0...v0.31.0)

### Features

* **api:** api update ([be81724](https://github.com/groq/groq-python/commit/be81724579d5538d340fe4f1bce9ab787ef2e387))
* **api:** api update ([bd9eafd](https://github.com/groq/groq-python/commit/bd9eafd4ef5ff1379c4a716fef023fbacfe0641e))
* **api:** api update ([86eab4f](https://github.com/groq/groq-python/commit/86eab4f85c8e515cd54dfd163d694237f2d6f118))
* **api:** api update ([4068695](https://github.com/groq/groq-python/commit/4068695a917367872432d6b35985692c87dd8faa))
* **api:** api update ([5c45441](https://github.com/groq/groq-python/commit/5c45441126fa94690e4fcbeab497d2c07cf54e50))
* **api:** api update ([30646f2](https://github.com/groq/groq-python/commit/30646f2f85dd6cf328b61628d2c9dac970299d28))
* **api:** api update ([e8ede14](https://github.com/groq/groq-python/commit/e8ede14f50b999ebc9d39da2881f7f59c3aa8b4a))
* **api:** api update ([3c06879](https://github.com/groq/groq-python/commit/3c068790ee3632a58f8da9cfb45d1055b8ac9058))
* **api:** api update ([455c74a](https://github.com/groq/groq-python/commit/455c74a13f0552b9e9abc08a8ddcf40b34a654cc))
* clean up environment call outs ([0627bc6](https://github.com/groq/groq-python/commit/0627bc60fd9c038ae47e63a1bf3a36557157ed9e))
* **client:** support file upload requests ([0f2d5a7](https://github.com/groq/groq-python/commit/0f2d5a78551a91aedd44160126ec85b833a7682b))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([7439911](https://github.com/groq/groq-python/commit/74399119e020f45a154f5cdf46bdd63b476090e9))
* **parsing:** ignore empty metadata ([eccd423](https://github.com/groq/groq-python/commit/eccd42322df3347194b64688f222518b56acb7f9))
* **parsing:** parse extra field types ([590a947](https://github.com/groq/groq-python/commit/590a947ec17aca23ce82f546ee9c25800a7061ff))
* streaming overrides ([ff828d6](https://github.com/groq/groq-python/commit/ff828d6363fae6b401dd47e696e7a2380226e051))


### Chores

* **project:** add settings file for vscode ([938789a](https://github.com/groq/groq-python/commit/938789a2545daec2fd9eb5b0c0d612f2aac6419b))

## 0.30.0 (2025-07-11)

Full Changelog: [v0.29.0...v0.30.0](https://github.com/groq/groq-python/compare/v0.29.0...v0.30.0)

### Features

* **api:** api update ([55abbbc](https://github.com/groq/groq-python/commit/55abbbc39b85f5f179ce698b67d493e0ad359773))
* **api:** api update ([cbd7df0](https://github.com/groq/groq-python/commit/cbd7df040d8b70d22ba5527d29a915459c69d482))


### Bug Fixes

* **ci:** correct conditional ([a470509](https://github.com/groq/groq-python/commit/a4705094213290bf95c599dbfe30be078d584677))
* **ci:** release-doctor — report correct token name ([b036bba](https://github.com/groq/groq-python/commit/b036bba0a7e3a306cb9849fc701fce32aec00501))
* **parsing:** correctly handle nested discriminated unions ([f57dd03](https://github.com/groq/groq-python/commit/f57dd033543b07c24a6c2ae11d8e7303e3888cd7))
* performance tier enum overloads ([dc7c41b](https://github.com/groq/groq-python/commit/dc7c41bdfc2759e36711d6faae0c3e29d8882b84))


### Chores

* Add bklieger-groq to CODEOWNERS ([5b9fc30](https://github.com/groq/groq-python/commit/5b9fc30d6aa58a9b9fd3eb32b79618f4551316e2))
* **ci:** change upload type ([7044a2b](https://github.com/groq/groq-python/commit/7044a2b6fbdb996aab8e11a9c56bcbccb72530dc))
* **ci:** only run for pushes and fork pull requests ([dc1b9ee](https://github.com/groq/groq-python/commit/dc1b9eea773fe7d9c8f972ad375024a99e03a58f))
* fix code owners ([464ada9](https://github.com/groq/groq-python/commit/464ada9d4cde3fb7525e383e747178c94348472d))
* **internal:** bump pinned h11 dep ([47bddbd](https://github.com/groq/groq-python/commit/47bddbdf76ec98464b97886d5e6c0fd5f25af453))
* **internal:** codegen related update ([9d7f071](https://github.com/groq/groq-python/commit/9d7f071f7947f7895258bdee533e0e99f20aa5b8))
* **package:** mark python 3.13 as supported ([55353b9](https://github.com/groq/groq-python/commit/55353b9f792db825a7b14be2221e342a11261c59))
* **readme:** fix version rendering on pypi ([e145b51](https://github.com/groq/groq-python/commit/e145b5135125b25f1a0a5856dcf1223503882590))

## 0.29.0 (2025-06-25)

Full Changelog: [v0.28.0...v0.29.0](https://github.com/groq/groq-python/compare/v0.28.0...v0.29.0)

### Features

* **api:** api update ([2f78465](https://github.com/groq/groq-python/commit/2f7846558486855edc4001eefc6bec003a943d26))
* **client:** add support for aiohttp ([a306987](https://github.com/groq/groq-python/commit/a30698732eeaa097832132908429c6b04e7cf027))


### Bug Fixes

* **client:** correctly parse binary response | stream ([da571bc](https://github.com/groq/groq-python/commit/da571bc0979873525bbf9c2d6efa53aee27a8519))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([778531f](https://github.com/groq/groq-python/commit/778531f0de3f65881b226bf42b93cac119d3f209))


### Chores

* **ci:** enable for pull requests ([daf0500](https://github.com/groq/groq-python/commit/daf050078783c0389c950d422335533d85320cf6))
* **internal:** update conftest.py ([ed4b0b5](https://github.com/groq/groq-python/commit/ed4b0b59bc0bc63363f46d2baed8ff833470130e))
* **readme:** update badges ([d08d4f4](https://github.com/groq/groq-python/commit/d08d4f4472e452eaa92ed1385342cb01b1a0797d))
* **tests:** add tests for httpx client instantiation & proxies ([94821d3](https://github.com/groq/groq-python/commit/94821d3c726bb3ca7057c7a19958e6111789c9de))
* **tests:** run tests in parallel ([ce56989](https://github.com/groq/groq-python/commit/ce56989094581c26b79605012c637e942c972689))
* **tests:** skip some failing tests on the latest python versions ([15a744b](https://github.com/groq/groq-python/commit/15a744b4ce1043d3e17dfee8bcae329f5708e6c8))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([5776227](https://github.com/groq/groq-python/commit/577622772f66242961d216dffef1d6e003028d7f))

## 0.28.0 (2025-06-12)

Full Changelog: [v0.27.0...v0.28.0](https://github.com/groq/groq-python/compare/v0.27.0...v0.28.0)

### Features

* **api:** api update ([1b088b1](https://github.com/groq/groq-python/commit/1b088b11e42ddd9b04c3fa9fc0d1cf957696529a))
* **api:** api update ([2a96d4f](https://github.com/groq/groq-python/commit/2a96d4fbcf6dbff9a8125a0f5f9d73ffe97d5223))
* **api:** api update ([089ab40](https://github.com/groq/groq-python/commit/089ab404ada560ca59048ec23981252f439165ea))


### Chores

* fix streaming overloads ([bb31101](https://github.com/groq/groq-python/commit/bb3110118ca7fe8258d7eaed6856a1bed560e533))

## 0.27.0 (2025-06-10)

Full Changelog: [v0.26.0...v0.27.0](https://github.com/groq/groq-python/compare/v0.26.0...v0.27.0)

### Features

* **api:** api update ([3f311d6](https://github.com/groq/groq-python/commit/3f311d6f1ae14a788bbd603fdca9552e3092ec9f))
* **client:** add follow_redirects request option ([407d5f6](https://github.com/groq/groq-python/commit/407d5f6f6c192289f6822e91f92d15fdae613a7a))


### Chores

* **docs:** remove reference to rye shell ([69a126e](https://github.com/groq/groq-python/commit/69a126e1cbcba19793dcfebf8222351427ce8a28))
* **docs:** remove unnecessary param examples ([f645e86](https://github.com/groq/groq-python/commit/f645e86baca1d5a5ba8e26f7a54427554f0ffe85))

## 0.26.0 (2025-05-29)

Full Changelog: [v0.25.0...v0.26.0](https://github.com/groq/groq-python/compare/v0.25.0...v0.26.0)

### Features

* **api:** api update ([52000cb](https://github.com/groq/groq-python/commit/52000cb906e1163c589a4000f916da979d3da50b))
* **api:** api update ([6718a54](https://github.com/groq/groq-python/commit/6718a549eeaefb681dea7a0494cbeb1480461281))


### Chores

* **docs:** grammar improvements ([b5f3b46](https://github.com/groq/groq-python/commit/b5f3b462124c56b1360027f1b86aa4ea9fc189f1))

## 0.25.0 (2025-05-16)

Full Changelog: [v0.24.0...v0.25.0](https://github.com/groq/groq-python/compare/v0.24.0...v0.25.0)

### Features

* **api:** api update ([385969a](https://github.com/groq/groq-python/commit/385969a478242c67dd07e510632ea1f168f743d8))
* **api:** api update ([e3acb61](https://github.com/groq/groq-python/commit/e3acb618e09864829089575c51ec617b2f4b6975))
* **api:** api update ([4bb39e5](https://github.com/groq/groq-python/commit/4bb39e59bbd317de95b3e1d896ab83ee41bc7b3e))
* **api:** api update ([ce3c251](https://github.com/groq/groq-python/commit/ce3c2514e2e66557de3e583532743cb3806032a2))


### Bug Fixes

* add search settings to all chat completion overloads ([32a1731](https://github.com/groq/groq-python/commit/32a17310c3a481b4b6b7aaa1f742720c367864f5))
* GitHub Terraform: Create/Update .github/workflows/stale.yaml [skip ci] ([a365e26](https://github.com/groq/groq-python/commit/a365e262f988103f5757ffd9054b822a72868586))
* **package:** support direct resource imports ([3ee8779](https://github.com/groq/groq-python/commit/3ee87792c92196abba0a1c7d9400a34d95c58895))


### Chores

* **ci:** fix installation instructions ([454ff60](https://github.com/groq/groq-python/commit/454ff60a12d7e16127d87ef9c152b9e4a394246d))
* **ci:** upload sdks to package manager ([1f464f8](https://github.com/groq/groq-python/commit/1f464f84bee361e07214e6b65a6727a1b5e0bc7b))
* fix README example ([7a0f06a](https://github.com/groq/groq-python/commit/7a0f06aca6223dc04e146f1b75445a2a64ce409a))
* **internal:** avoid errors for isinstance checks on proxies ([7a04964](https://github.com/groq/groq-python/commit/7a04964d964feaac9dfcf1f46dad1f63a5acf714))
* use lazy imports for resources ([8c6351a](https://github.com/groq/groq-python/commit/8c6351a0215827dea34174978a78d06a528e6eef))


### Documentation

* remove or fix invalid readme examples ([4dc027a](https://github.com/groq/groq-python/commit/4dc027a35054db11eec6c8bfe1fd463b0c49db6e))

## 0.24.0 (2025-05-02)

Full Changelog: [v0.23.1...v0.24.0](https://github.com/groq/groq-python/compare/v0.23.1...v0.24.0)

### Features

* **api:** api update ([e65ff4d](https://github.com/groq/groq-python/commit/e65ff4d299fd612b6ce04e5cf5544b93bbc45297))


### Bug Fixes

* add include/exclude_domains to all chat completions overloads ([7616f4b](https://github.com/groq/groq-python/commit/7616f4b2e91db267a6afe0700511b324471f9983))

## 0.23.1 (2025-04-24)

Full Changelog: [v0.23.0...v0.23.1](https://github.com/groq/groq-python/compare/v0.23.0...v0.23.1)

### Bug Fixes

* add executed_tools to streaming choicedelta ([fb26fbc](https://github.com/groq/groq-python/commit/fb26fbcd0b141a6d33b95beed870b8a814a02f12))
* **pydantic v1:** more robust ModelField.annotation check ([40aaee2](https://github.com/groq/groq-python/commit/40aaee2cd755ab3e1c7a11b5744eecaa2c66b0b6))


### Chores

* broadly detect json family of content-type headers ([2411533](https://github.com/groq/groq-python/commit/24115339497fd35b19800abeca4d5527573f2807))
* **ci:** add timeout thresholds for CI jobs ([aae4614](https://github.com/groq/groq-python/commit/aae461436e635710f2fccf3c45e7d66ab270958e))
* **ci:** only use depot for staging repos ([b6d1b47](https://github.com/groq/groq-python/commit/b6d1b47c1c064c4af93ace21247edacd6bf1b913))
* **internal:** codegen related update ([1da64f5](https://github.com/groq/groq-python/commit/1da64f5c788477d3a0d0514b2ef13e5edbbdda49))
* **internal:** fix list file params ([a9b18de](https://github.com/groq/groq-python/commit/a9b18debf828ca3717c5cfd8085904d8bce70e57))
* **internal:** import reformatting ([5068736](https://github.com/groq/groq-python/commit/506873683250e242bf05e3d99eca03a38257e082))
* **internal:** minor formatting changes ([bc26d60](https://github.com/groq/groq-python/commit/bc26d603a592529f76502b52f313d1e36bbb2645))
* **internal:** refactor retries to not use recursion ([488b9fe](https://github.com/groq/groq-python/commit/488b9fe0a8ae9267a40e545a7a4c265b461e841c))

## 0.23.0 (2025-04-22)

Full Changelog: [v0.22.0...v0.23.0](https://github.com/groq/groq-python/compare/v0.22.0...v0.23.0)

### Features

* **api:** api update ([f5cbd01](https://github.com/groq/groq-python/commit/f5cbd0148e81de278728b3b78a409ad752ec812b))
* **api:** api update ([e7c5514](https://github.com/groq/groq-python/commit/e7c5514b3e4b60a6346500d30620ba9c49b7ac7e))
* **api:** api update ([9d5b7c8](https://github.com/groq/groq-python/commit/9d5b7c8ba4249f57eb17d02c8e18aa46ad5f6d10))
* **api:** api update ([73357e1](https://github.com/groq/groq-python/commit/73357e15c4ab1505e7f370ede8bd408883967e1b))
* **api:** api update ([b1d6697](https://github.com/groq/groq-python/commit/b1d66973010bf3ba63b11744df08da6b8a770841))
* **api:** api update ([98ef30e](https://github.com/groq/groq-python/commit/98ef30efd2e30716c732a62159f3f33f441f4b5f))


### Bug Fixes

* **perf:** optimize some hot paths ([b1bd305](https://github.com/groq/groq-python/commit/b1bd305b5b91fa8473661b061aa4c01a2c310249))
* **perf:** skip traversing types for NotGiven values ([ea1b705](https://github.com/groq/groq-python/commit/ea1b705b27465710aaf482efc581df593d727864))


### Chores

* **client:** minor internal fixes ([68c2947](https://github.com/groq/groq-python/commit/68c2947a7eafe6265e8be5b38237e91615ecbe07))
* **internal:** base client updates ([d83d3a7](https://github.com/groq/groq-python/commit/d83d3a79bd53b7adf6b0d36ec85940c4455c71fe))
* **internal:** bump pyright version ([49dc519](https://github.com/groq/groq-python/commit/49dc51915a973284e1a5a335ba2663d534a8dad7))
* **internal:** expand CI branch coverage ([ed6a533](https://github.com/groq/groq-python/commit/ed6a5331f2a72de6487ec689992bebff4e89a25c))
* **internal:** reduce CI branch coverage ([0139f63](https://github.com/groq/groq-python/commit/0139f63299b4f251b9cd9267ffdea4c809694d50))
* **internal:** remove trailing character ([#233](https://github.com/groq/groq-python/issues/233)) ([2781f14](https://github.com/groq/groq-python/commit/2781f1439e025b088651520c6c24bdb6cec0568b))
* **internal:** slight transform perf improvement ([#235](https://github.com/groq/groq-python/issues/235)) ([c67eeaa](https://github.com/groq/groq-python/commit/c67eeaabfc20960ad1c25eb425193009d9b6fc35))
* **internal:** update models test ([0ce3c37](https://github.com/groq/groq-python/commit/0ce3c379c8d3f8b1745d0d38e850cf2a7122d3e7))
* **internal:** update pyright settings ([66d55ee](https://github.com/groq/groq-python/commit/66d55eeeac41543a0f0fb9f5bad52ecc46ad79f7))
* slight wording improvement in README ([#237](https://github.com/groq/groq-python/issues/237)) ([fa001a3](https://github.com/groq/groq-python/commit/fa001a3e9228ea6b734a33394a14edf32f70c528))
* **tests:** improve enum examples ([#236](https://github.com/groq/groq-python/issues/236)) ([6218620](https://github.com/groq/groq-python/commit/62186208c2c5971a7fc7ea0e4519ec7c002dc84f))

## 0.22.0 (2025-04-02)

Full Changelog: [v0.21.0...v0.22.0](https://github.com/groq/groq-python/compare/v0.21.0...v0.22.0)

### Features

* **api:** add batch cancellation ([a5c3827](https://github.com/groq/groq-python/commit/a5c3827126e788d4f6822e63cda08eef43412d1b))

## 0.21.0 (2025-04-01)

Full Changelog: [v0.20.0...v0.21.0](https://github.com/groq/groq-python/compare/v0.20.0...v0.21.0)

### Features

* **api:** api update ([#224](https://github.com/groq/groq-python/issues/224)) ([94f29cf](https://github.com/groq/groq-python/commit/94f29cfa5a5873d46de380de98b3bb37aff78615))
* **api:** api update ([#225](https://github.com/groq/groq-python/issues/225)) ([cdf668c](https://github.com/groq/groq-python/commit/cdf668c5b45ea5bef841f2e2da38664c09454a55))
* **api:** manual updates ([#226](https://github.com/groq/groq-python/issues/226)) ([499e454](https://github.com/groq/groq-python/commit/499e4544aa45a25f333de8b34714dbaa5242dcbc))


### Chores

* fix typos ([#222](https://github.com/groq/groq-python/issues/222)) ([51bb8ad](https://github.com/groq/groq-python/commit/51bb8ad9c5826d72ecaa95bd00d36f86fc1b5b98))

## 0.20.0 (2025-03-19)

Full Changelog: [v0.19.0...v0.20.0](https://github.com/groq/groq-python/compare/v0.19.0...v0.20.0)

### Features

* **api:** Add speech endpoint ([#219](https://github.com/groq/groq-python/issues/219)) ([f150801](https://github.com/groq/groq-python/commit/f150801968535bafe87794addf01ae4beaec8351))
* **api:** api update ([#218](https://github.com/groq/groq-python/issues/218)) ([c124862](https://github.com/groq/groq-python/commit/c124862e24b820569a777c86a4e14c7e1c69fa2d))
* **api:** api update ([#220](https://github.com/groq/groq-python/issues/220)) ([f4eeb8d](https://github.com/groq/groq-python/commit/f4eeb8d8be6a08b2432b3941d7c730d055447c4e))


### Bug Fixes

* **ci:** ensure pip is always available ([#216](https://github.com/groq/groq-python/issues/216)) ([085166c](https://github.com/groq/groq-python/commit/085166c1293b26bea8f09d5be4f11d3db9f18497))
* **ci:** remove publishing patch ([#217](https://github.com/groq/groq-python/issues/217)) ([fb579e8](https://github.com/groq/groq-python/commit/fb579e87a36d153263ea01b566b4ed7fb967eaf5))
* **types:** handle more discriminated union shapes ([#215](https://github.com/groq/groq-python/issues/215)) ([5c72e94](https://github.com/groq/groq-python/commit/5c72e94d51f34b694a5e00665dcc76af72e5d1da))


### Chores

* **internal:** bump rye to 0.44.0 ([#214](https://github.com/groq/groq-python/issues/214)) ([66feae2](https://github.com/groq/groq-python/commit/66feae21c5762518bed3b1cc8f61ced4963d7ea3))
* **internal:** codegen related update ([#213](https://github.com/groq/groq-python/issues/213)) ([7a16274](https://github.com/groq/groq-python/commit/7a1627444b004d3d5b9852739bec8376cbfc5a2c))
* **internal:** remove extra empty newlines ([#211](https://github.com/groq/groq-python/issues/211)) ([4187fa1](https://github.com/groq/groq-python/commit/4187fa110ff477e8bb6b313ca3dd8d8227dffb84))

## 0.19.0 (2025-03-11)

Full Changelog: [v0.18.0...v0.19.0](https://github.com/groq/groq-python/compare/v0.18.0...v0.19.0)

### Features

* **api:** manual updates ([#209](https://github.com/groq/groq-python/issues/209)) ([15e2dca](https://github.com/groq/groq-python/commit/15e2dca833561464c7f56b3b5ce4de2bb4a90dfe))
* **client:** allow passing `NotGiven` for body ([#200](https://github.com/groq/groq-python/issues/200)) ([afa6c0f](https://github.com/groq/groq-python/commit/afa6c0fc0191cedbacf99a7c6ac662d888ba9ffd))
* **client:** send `X-Stainless-Read-Timeout` header ([#193](https://github.com/groq/groq-python/issues/193)) ([e8911a4](https://github.com/groq/groq-python/commit/e8911a43d64861153306bd03cfdaa06670b335f5))


### Bug Fixes

* add reasoning field to ChoiceDelta class ([edfee3b](https://github.com/groq/groq-python/commit/edfee3b6c5976da372908fcb0cd02e91f5b0cea3))
* asyncify on non-asyncio runtimes ([#198](https://github.com/groq/groq-python/issues/198)) ([49387fe](https://github.com/groq/groq-python/commit/49387fe83c2886f6c623f7718f041c0065829a2b))
* **client:** mark some request bodies as optional ([afa6c0f](https://github.com/groq/groq-python/commit/afa6c0fc0191cedbacf99a7c6ac662d888ba9ffd))
* GitHub Terraform: Create/Update .github/workflows/stale.yaml [skip ci] ([662763a](https://github.com/groq/groq-python/commit/662763a5eaf833226772dedb36f64cfd460901a1))
* GitHub Terraform: Create/Update .github/workflows/stale.yaml [skip ci] ([5298ec1](https://github.com/groq/groq-python/commit/5298ec1a8c6f1b6958a217c95f6a8bb19e90bd28))


### Chores

* **api:** remove chat_completion_chunk to force a rebuild of it ([#208](https://github.com/groq/groq-python/issues/208)) ([01fb0d1](https://github.com/groq/groq-python/commit/01fb0d14e438eeaef6ab1518a0c49e5b5b8e7197))
* **docs:** update client docstring ([#204](https://github.com/groq/groq-python/issues/204)) ([a0f4599](https://github.com/groq/groq-python/commit/a0f45996ff149e0ed6f1fc262eb7041297b4bd68))
* **internal:** codegen related update ([#199](https://github.com/groq/groq-python/issues/199)) ([de2ac71](https://github.com/groq/groq-python/commit/de2ac71d68109c3b29e6de1ba97f2c7092881c42))
* **internal:** fix devcontainers setup ([#201](https://github.com/groq/groq-python/issues/201)) ([af101ee](https://github.com/groq/groq-python/commit/af101ee282a335d9f7970a92a99f6b63db9aebd8))
* **internal:** fix type traversing dictionary params ([#195](https://github.com/groq/groq-python/issues/195)) ([bcb0256](https://github.com/groq/groq-python/commit/bcb025668a8b7279b8dbfb79384b1a20b95cd57f))
* **internal:** minor type handling changes ([#196](https://github.com/groq/groq-python/issues/196)) ([3ff53df](https://github.com/groq/groq-python/commit/3ff53df5cc754090a645babff1f3e5d636f9e71c))
* **internal:** properly set __pydantic_private__ ([#202](https://github.com/groq/groq-python/issues/202)) ([07ec0c8](https://github.com/groq/groq-python/commit/07ec0c885d7998717a2702de08dd5f1a4ee397ec))
* **internal:** remove unused http client options forwarding ([#205](https://github.com/groq/groq-python/issues/205)) ([12fdb59](https://github.com/groq/groq-python/commit/12fdb59dbcaa121710f5c5ea710ff0f14c8c6dce))
* **internal:** update client tests ([#197](https://github.com/groq/groq-python/issues/197)) ([2f0d2c4](https://github.com/groq/groq-python/commit/2f0d2c475a11d7162dffbb31008f01b17b2c8ef4))


### Documentation

* revise readme docs about nested params ([#206](https://github.com/groq/groq-python/issues/206)) ([7b04f47](https://github.com/groq/groq-python/commit/7b04f472fa2a203cda9747308920974ed427f0ed))
* update URLs from stainlessapi.com to stainless.com ([#203](https://github.com/groq/groq-python/issues/203)) ([a6c6fde](https://github.com/groq/groq-python/commit/a6c6fde2ae256469481a28b59beaed1ab1f61c96))

## 0.18.0 (2025-02-05)

Full Changelog: [v0.17.0...v0.18.0](https://github.com/groq/groq-python/compare/v0.17.0...v0.18.0)

### Features

* **api:** Add batch API ([#191](https://github.com/groq/groq-python/issues/191)) ([367a744](https://github.com/groq/groq-python/commit/367a744f461ec82353b916c7d95224d9baa78737))


### Chores

* **internal:** bummp ruff dependency ([#190](https://github.com/groq/groq-python/issues/190)) ([61678fc](https://github.com/groq/groq-python/commit/61678fc5fd4eb42e42d88057934b6204d19086af))
* **internal:** change default timeout to an int ([#188](https://github.com/groq/groq-python/issues/188)) ([348e152](https://github.com/groq/groq-python/commit/348e1526711e4d162379dcd80a9b201572508376))

## 0.17.0 (2025-02-03)

Full Changelog: [v0.16.0...v0.17.0](https://github.com/groq/groq-python/compare/v0.16.0...v0.17.0)

### Features

* **api:** api update ([#185](https://github.com/groq/groq-python/issues/185)) ([e237339](https://github.com/groq/groq-python/commit/e2373395cf89c48bb766bedca91e1af7d9b5036f))

## 0.16.0 (2025-01-29)

Full Changelog: [v0.15.0...v0.16.0](https://github.com/groq/groq-python/compare/v0.15.0...v0.16.0)

### Features

* **api:** api update ([#183](https://github.com/groq/groq-python/issues/183)) ([a5cdbc5](https://github.com/groq/groq-python/commit/a5cdbc5af797bdb3aa9733c60f733e612d619ef5))


### Chores

* **internal:** codegen related update ([#177](https://github.com/groq/groq-python/issues/177)) ([01e6304](https://github.com/groq/groq-python/commit/01e63041c81099bf0fb64a372462be71767fb747))
* **internal:** codegen related update ([#180](https://github.com/groq/groq-python/issues/180)) ([5c8db1a](https://github.com/groq/groq-python/commit/5c8db1a9795dfad7316a9c1e026386a0ad62e3db))
* **internal:** minor formatting changes ([#182](https://github.com/groq/groq-python/issues/182)) ([2c4e409](https://github.com/groq/groq-python/commit/2c4e409fe047cb2cc9ca3805f79244c1fdbb7cf0))
* **internal:** minor style changes ([#181](https://github.com/groq/groq-python/issues/181)) ([77c752a](https://github.com/groq/groq-python/commit/77c752ab1a635b675743baf02d4896439bc85a07))


### Documentation

* **raw responses:** fix duplicate `the` ([#179](https://github.com/groq/groq-python/issues/179)) ([a28cbd8](https://github.com/groq/groq-python/commit/a28cbd863d875954a0404ff1148da02cd131de98))

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
