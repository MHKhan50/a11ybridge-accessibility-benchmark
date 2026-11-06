# Results

## Share of runs by outcome (%)

| Model | Lang | Element | Defect | n | Target | Risky look-alike | Other wrong | Said none | Invalid |
|---|---|---|---|---|---|---|---|---|---|
| llama3.1:8b | en | button | baseline | 16 | 100 | 0 | 0 | 0 | 0 |
| llama3.1:8b | en | button | div_not_button | 16 | 94 | 0 | 6 | 0 | 0 |
| llama3.1:8b | en | button | duplicate_name | 16 | 88 | 0 | 12 | 0 | 0 |
| llama3.1:8b | en | button | generic_name | 16 | 50 | 6 | 44 | 0 | 0 |
| llama3.1:8b | en | button | icon_no_name | 16 | 19 | 0 | 81 | 0 | 0 |
| llama3.1:8b | en | button | img_no_alt | 16 | 12 | 0 | 81 | 6 | 0 |
| llama3.1:8b | en | link | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| llama3.1:8b | en | link | duplicate_name | 8 | 38 | 0 | 62 | 0 | 0 |
| llama3.1:8b | en | link | generic_name | 8 | 12 | 0 | 75 | 12 | 0 |
| llama3.1:8b | en | link | img_no_alt | 8 | 12 | 12 | 75 | 0 | 0 |
| llama3.1:8b | en | link | span_not_link | 8 | 100 | 0 | 0 | 0 | 0 |
| llama3.1:8b | en | textbox | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| llama3.1:8b | en | textbox | label_not_linked | 8 | 12 | 0 | 88 | 0 | 0 |
| llama3.1:8b | en | textbox | no_label | 8 | 12 | 0 | 38 | 50 | 0 |
| llama3.1:8b | en | textbox | placeholder_only | 8 | 100 | 0 | 0 | 0 | 0 |
| llama3.1:8b | ru | button | baseline | 16 | 100 | 0 | 0 | 0 | 0 |
| llama3.1:8b | ru | button | div_not_button | 16 | 100 | 0 | 0 | 0 | 0 |
| llama3.1:8b | ru | button | duplicate_name | 16 | 81 | 6 | 12 | 0 | 0 |
| llama3.1:8b | ru | button | generic_name | 16 | 25 | 19 | 31 | 25 | 0 |
| llama3.1:8b | ru | button | icon_no_name | 16 | 12 | 19 | 44 | 25 | 0 |
| llama3.1:8b | ru | button | img_no_alt | 16 | 6 | 19 | 50 | 25 | 0 |
| llama3.1:8b | ru | link | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| llama3.1:8b | ru | link | duplicate_name | 8 | 50 | 0 | 50 | 0 | 0 |
| llama3.1:8b | ru | link | generic_name | 8 | 12 | 0 | 75 | 12 | 0 |
| llama3.1:8b | ru | link | img_no_alt | 8 | 12 | 12 | 75 | 0 | 0 |
| llama3.1:8b | ru | link | span_not_link | 8 | 100 | 0 | 0 | 0 | 0 |
| llama3.1:8b | ru | textbox | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| llama3.1:8b | ru | textbox | label_not_linked | 8 | 38 | 0 | 62 | 0 | 0 |
| llama3.1:8b | ru | textbox | no_label | 8 | 38 | 0 | 12 | 50 | 0 |
| llama3.1:8b | ru | textbox | placeholder_only | 8 | 100 | 0 | 0 | 0 | 0 |
| llama3.2:3b | en | button | baseline | 16 | 100 | 0 | 0 | 0 | 0 |
| llama3.2:3b | en | button | div_not_button | 16 | 94 | 0 | 6 | 0 | 0 |
| llama3.2:3b | en | button | duplicate_name | 16 | 75 | 0 | 25 | 0 | 0 |
| llama3.2:3b | en | button | generic_name | 16 | 19 | 6 | 62 | 12 | 0 |
| llama3.2:3b | en | button | icon_no_name | 16 | 0 | 31 | 69 | 0 | 0 |
| llama3.2:3b | en | button | img_no_alt | 16 | 0 | 12 | 88 | 0 | 0 |
| llama3.2:3b | en | link | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| llama3.2:3b | en | link | duplicate_name | 8 | 12 | 0 | 88 | 0 | 0 |
| llama3.2:3b | en | link | generic_name | 8 | 0 | 0 | 75 | 25 | 0 |
| llama3.2:3b | en | link | img_no_alt | 8 | 0 | 0 | 88 | 12 | 0 |
| llama3.2:3b | en | link | span_not_link | 8 | 62 | 12 | 25 | 0 | 0 |
| llama3.2:3b | en | textbox | baseline | 8 | 88 | 0 | 12 | 0 | 0 |
| llama3.2:3b | en | textbox | label_not_linked | 8 | 50 | 0 | 50 | 0 | 0 |
| llama3.2:3b | en | textbox | no_label | 8 | 12 | 0 | 75 | 12 | 0 |
| llama3.2:3b | en | textbox | placeholder_only | 8 | 88 | 0 | 12 | 0 | 0 |
| llama3.2:3b | ru | button | baseline | 16 | 81 | 0 | 19 | 0 | 0 |
| llama3.2:3b | ru | button | div_not_button | 16 | 69 | 0 | 31 | 0 | 0 |
| llama3.2:3b | ru | button | duplicate_name | 16 | 31 | 6 | 62 | 0 | 0 |
| llama3.2:3b | ru | button | generic_name | 16 | 12 | 6 | 81 | 0 | 0 |
| llama3.2:3b | ru | button | icon_no_name | 16 | 0 | 19 | 81 | 0 | 0 |
| llama3.2:3b | ru | button | img_no_alt | 16 | 6 | 6 | 88 | 0 | 0 |
| llama3.2:3b | ru | link | baseline | 8 | 75 | 0 | 25 | 0 | 0 |
| llama3.2:3b | ru | link | duplicate_name | 8 | 0 | 12 | 75 | 12 | 0 |
| llama3.2:3b | ru | link | generic_name | 8 | 12 | 12 | 75 | 0 | 0 |
| llama3.2:3b | ru | link | img_no_alt | 8 | 0 | 12 | 88 | 0 | 0 |
| llama3.2:3b | ru | link | span_not_link | 8 | 62 | 12 | 25 | 0 | 0 |
| llama3.2:3b | ru | textbox | baseline | 8 | 75 | 0 | 25 | 0 | 0 |
| llama3.2:3b | ru | textbox | label_not_linked | 8 | 62 | 0 | 38 | 0 | 0 |
| llama3.2:3b | ru | textbox | no_label | 8 | 12 | 0 | 62 | 25 | 0 |
| llama3.2:3b | ru | textbox | placeholder_only | 8 | 62 | 0 | 38 | 0 | 0 |
| mistral:7b | en | button | baseline | 16 | 100 | 0 | 0 | 0 | 0 |
| mistral:7b | en | button | div_not_button | 16 | 100 | 0 | 0 | 0 | 0 |
| mistral:7b | en | button | duplicate_name | 16 | 69 | 6 | 25 | 0 | 0 |
| mistral:7b | en | button | generic_name | 16 | 19 | 0 | 6 | 75 | 0 |
| mistral:7b | en | button | icon_no_name | 16 | 0 | 0 | 6 | 94 | 0 |
| mistral:7b | en | button | img_no_alt | 16 | 0 | 0 | 0 | 100 | 0 |
| mistral:7b | en | link | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| mistral:7b | en | link | duplicate_name | 8 | 38 | 0 | 62 | 0 | 0 |
| mistral:7b | en | link | generic_name | 8 | 0 | 0 | 50 | 50 | 0 |
| mistral:7b | en | link | img_no_alt | 8 | 0 | 0 | 50 | 50 | 0 |
| mistral:7b | en | link | span_not_link | 8 | 88 | 0 | 12 | 0 | 0 |
| mistral:7b | en | textbox | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| mistral:7b | en | textbox | label_not_linked | 8 | 88 | 0 | 12 | 0 | 0 |
| mistral:7b | en | textbox | no_label | 8 | 12 | 0 | 38 | 50 | 0 |
| mistral:7b | en | textbox | placeholder_only | 8 | 100 | 0 | 0 | 0 | 0 |
| mistral:7b | ru | button | baseline | 16 | 94 | 6 | 0 | 0 | 0 |
| mistral:7b | ru | button | div_not_button | 16 | 94 | 0 | 0 | 6 | 0 |
| mistral:7b | ru | button | duplicate_name | 16 | 56 | 6 | 38 | 0 | 0 |
| mistral:7b | ru | button | generic_name | 16 | 19 | 0 | 25 | 56 | 0 |
| mistral:7b | ru | button | icon_no_name | 16 | 0 | 0 | 25 | 75 | 0 |
| mistral:7b | ru | button | img_no_alt | 16 | 0 | 6 | 31 | 62 | 0 |
| mistral:7b | ru | link | baseline | 8 | 62 | 0 | 38 | 0 | 0 |
| mistral:7b | ru | link | duplicate_name | 8 | 25 | 0 | 62 | 12 | 0 |
| mistral:7b | ru | link | generic_name | 8 | 0 | 0 | 50 | 50 | 0 |
| mistral:7b | ru | link | img_no_alt | 8 | 0 | 0 | 50 | 50 | 0 |
| mistral:7b | ru | link | span_not_link | 8 | 50 | 0 | 50 | 0 | 0 |
| mistral:7b | ru | textbox | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| mistral:7b | ru | textbox | label_not_linked | 8 | 88 | 0 | 12 | 0 | 0 |
| mistral:7b | ru | textbox | no_label | 8 | 25 | 0 | 50 | 25 | 0 |
| mistral:7b | ru | textbox | placeholder_only | 8 | 88 | 0 | 0 | 12 | 0 |
| qwen2.5:3b | en | button | baseline | 16 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:3b | en | button | div_not_button | 16 | 94 | 0 | 6 | 0 | 0 |
| qwen2.5:3b | en | button | duplicate_name | 16 | 62 | 0 | 38 | 0 | 0 |
| qwen2.5:3b | en | button | generic_name | 16 | 6 | 44 | 6 | 44 | 0 |
| qwen2.5:3b | en | button | icon_no_name | 16 | 0 | 25 | 25 | 50 | 0 |
| qwen2.5:3b | en | button | img_no_alt | 16 | 12 | 12 | 31 | 44 | 0 |
| qwen2.5:3b | en | link | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:3b | en | link | duplicate_name | 8 | 25 | 0 | 75 | 0 | 0 |
| qwen2.5:3b | en | link | generic_name | 8 | 0 | 0 | 50 | 50 | 0 |
| qwen2.5:3b | en | link | img_no_alt | 8 | 0 | 0 | 50 | 50 | 0 |
| qwen2.5:3b | en | link | span_not_link | 8 | 75 | 0 | 25 | 0 | 0 |
| qwen2.5:3b | en | textbox | baseline | 8 | 88 | 0 | 12 | 0 | 0 |
| qwen2.5:3b | en | textbox | label_not_linked | 8 | 62 | 0 | 38 | 0 | 0 |
| qwen2.5:3b | en | textbox | no_label | 8 | 0 | 0 | 25 | 75 | 0 |
| qwen2.5:3b | en | textbox | placeholder_only | 8 | 25 | 0 | 75 | 0 | 0 |
| qwen2.5:3b | ru | button | baseline | 16 | 94 | 6 | 0 | 0 | 0 |
| qwen2.5:3b | ru | button | div_not_button | 16 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:3b | ru | button | duplicate_name | 16 | 50 | 0 | 50 | 0 | 0 |
| qwen2.5:3b | ru | button | generic_name | 16 | 19 | 6 | 0 | 75 | 0 |
| qwen2.5:3b | ru | button | icon_no_name | 16 | 0 | 12 | 6 | 81 | 0 |
| qwen2.5:3b | ru | button | img_no_alt | 16 | 0 | 6 | 6 | 88 | 0 |
| qwen2.5:3b | ru | link | baseline | 8 | 62 | 25 | 0 | 12 | 0 |
| qwen2.5:3b | ru | link | duplicate_name | 8 | 12 | 0 | 62 | 25 | 0 |
| qwen2.5:3b | ru | link | generic_name | 8 | 0 | 0 | 50 | 50 | 0 |
| qwen2.5:3b | ru | link | img_no_alt | 8 | 0 | 0 | 50 | 50 | 0 |
| qwen2.5:3b | ru | link | span_not_link | 8 | 75 | 0 | 25 | 0 | 0 |
| qwen2.5:3b | ru | textbox | baseline | 8 | 88 | 0 | 12 | 0 | 0 |
| qwen2.5:3b | ru | textbox | label_not_linked | 8 | 50 | 0 | 50 | 0 | 0 |
| qwen2.5:3b | ru | textbox | no_label | 8 | 0 | 0 | 25 | 75 | 0 |
| qwen2.5:3b | ru | textbox | placeholder_only | 8 | 38 | 0 | 62 | 0 | 0 |
| qwen2.5:7b | en | button | baseline | 16 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:7b | en | button | div_not_button | 16 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:7b | en | button | duplicate_name | 16 | 69 | 0 | 31 | 0 | 0 |
| qwen2.5:7b | en | button | generic_name | 16 | 44 | 6 | 12 | 38 | 0 |
| qwen2.5:7b | en | button | icon_no_name | 16 | 0 | 6 | 25 | 69 | 0 |
| qwen2.5:7b | en | button | img_no_alt | 16 | 0 | 12 | 38 | 50 | 0 |
| qwen2.5:7b | en | link | baseline | 8 | 88 | 0 | 12 | 0 | 0 |
| qwen2.5:7b | en | link | duplicate_name | 8 | 62 | 0 | 38 | 0 | 0 |
| qwen2.5:7b | en | link | generic_name | 8 | 0 | 0 | 50 | 50 | 0 |
| qwen2.5:7b | en | link | img_no_alt | 8 | 0 | 0 | 50 | 50 | 0 |
| qwen2.5:7b | en | link | span_not_link | 8 | 75 | 0 | 25 | 0 | 0 |
| qwen2.5:7b | en | textbox | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:7b | en | textbox | label_not_linked | 8 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:7b | en | textbox | no_label | 8 | 12 | 0 | 12 | 75 | 0 |
| qwen2.5:7b | en | textbox | placeholder_only | 8 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:7b | ru | button | baseline | 16 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:7b | ru | button | div_not_button | 16 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:7b | ru | button | duplicate_name | 16 | 88 | 0 | 12 | 0 | 0 |
| qwen2.5:7b | ru | button | generic_name | 16 | 38 | 12 | 19 | 31 | 0 |
| qwen2.5:7b | ru | button | icon_no_name | 16 | 0 | 6 | 44 | 50 | 0 |
| qwen2.5:7b | ru | button | img_no_alt | 16 | 0 | 19 | 38 | 44 | 0 |
| qwen2.5:7b | ru | link | baseline | 8 | 75 | 0 | 25 | 0 | 0 |
| qwen2.5:7b | ru | link | duplicate_name | 8 | 50 | 0 | 50 | 0 | 0 |
| qwen2.5:7b | ru | link | generic_name | 8 | 0 | 0 | 50 | 50 | 0 |
| qwen2.5:7b | ru | link | img_no_alt | 8 | 0 | 0 | 50 | 50 | 0 |
| qwen2.5:7b | ru | link | span_not_link | 8 | 62 | 0 | 38 | 0 | 0 |
| qwen2.5:7b | ru | textbox | baseline | 8 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:7b | ru | textbox | label_not_linked | 8 | 100 | 0 | 0 | 0 | 0 |
| qwen2.5:7b | ru | textbox | no_label | 8 | 38 | 0 | 38 | 25 | 0 |
| qwen2.5:7b | ru | textbox | placeholder_only | 8 | 100 | 0 | 0 | 0 | 0 |

## Paired differences in target choice (percentage points, bootstrap 95% CI)

| Model | Lang | Element | Comparison | Difference | 95% CI | Units |
|---|---|---|---|---|---|---|
| llama3.1:8b | en | button | div_not_button minus baseline | -6.2 | [-18.8, +0.0] | 16 |
| llama3.1:8b | en | button | duplicate_name minus baseline | -12.5 | [-31.2, +0.0] | 16 |
| llama3.1:8b | en | button | generic_name minus baseline | -50.0 | [-75.0, -25.0] | 16 |
| llama3.1:8b | en | button | icon_no_name minus baseline | -81.2 | [-100.0, -62.5] | 16 |
| llama3.1:8b | en | button | img_no_alt minus baseline | -87.5 | [-100.0, -68.8] | 16 |
| llama3.1:8b | en | link | duplicate_name minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| llama3.1:8b | en | link | generic_name minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| llama3.1:8b | en | link | img_no_alt minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| llama3.1:8b | en | link | span_not_link minus baseline | +0.0 | [+0.0, +0.0] | 8 |
| llama3.1:8b | en | textbox | label_not_linked minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| llama3.1:8b | en | textbox | no_label minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| llama3.1:8b | en | textbox | placeholder_only minus baseline | +0.0 | [+0.0, +0.0] | 8 |
| llama3.1:8b | ru | button | div_not_button minus baseline | +0.0 | [+0.0, +0.0] | 16 |
| llama3.1:8b | ru | button | duplicate_name minus baseline | -18.8 | [-37.5, +0.0] | 16 |
| llama3.1:8b | ru | button | generic_name minus baseline | -75.0 | [-93.8, -50.0] | 16 |
| llama3.1:8b | ru | button | icon_no_name minus baseline | -87.5 | [-100.0, -68.8] | 16 |
| llama3.1:8b | ru | button | img_no_alt minus baseline | -93.8 | [-100.0, -81.2] | 16 |
| llama3.1:8b | ru | link | duplicate_name minus baseline | -50.0 | [-87.5, -12.5] | 8 |
| llama3.1:8b | ru | link | generic_name minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| llama3.1:8b | ru | link | img_no_alt minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| llama3.1:8b | ru | link | span_not_link minus baseline | +0.0 | [+0.0, +0.0] | 8 |
| llama3.1:8b | ru | textbox | label_not_linked minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| llama3.1:8b | ru | textbox | no_label minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| llama3.1:8b | ru | textbox | placeholder_only minus baseline | +0.0 | [+0.0, +0.0] | 8 |
| llama3.2:3b | en | button | div_not_button minus baseline | -6.2 | [-18.8, +0.0] | 16 |
| llama3.2:3b | en | button | duplicate_name minus baseline | -25.0 | [-50.0, -6.2] | 16 |
| llama3.2:3b | en | button | generic_name minus baseline | -81.2 | [-100.0, -62.5] | 16 |
| llama3.2:3b | en | button | icon_no_name minus baseline | -100.0 | [-100.0, -100.0] | 16 |
| llama3.2:3b | en | button | img_no_alt minus baseline | -100.0 | [-100.0, -100.0] | 16 |
| llama3.2:3b | en | link | duplicate_name minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| llama3.2:3b | en | link | generic_name minus baseline | -100.0 | [-100.0, -100.0] | 8 |
| llama3.2:3b | en | link | img_no_alt minus baseline | -100.0 | [-100.0, -100.0] | 8 |
| llama3.2:3b | en | link | span_not_link minus baseline | -37.5 | [-75.0, -12.5] | 8 |
| llama3.2:3b | en | textbox | label_not_linked minus baseline | -37.5 | [-75.0, -12.5] | 8 |
| llama3.2:3b | en | textbox | no_label minus baseline | -75.0 | [-100.0, -37.5] | 8 |
| llama3.2:3b | en | textbox | placeholder_only minus baseline | +0.0 | [+0.0, +0.0] | 8 |
| llama3.2:3b | ru | button | div_not_button minus baseline | -12.5 | [-37.5, +12.5] | 16 |
| llama3.2:3b | ru | button | duplicate_name minus baseline | -50.0 | [-75.0, -25.0] | 16 |
| llama3.2:3b | ru | button | generic_name minus baseline | -68.8 | [-87.5, -43.8] | 16 |
| llama3.2:3b | ru | button | icon_no_name minus baseline | -81.2 | [-100.0, -62.5] | 16 |
| llama3.2:3b | ru | button | img_no_alt minus baseline | -75.0 | [-93.8, -56.2] | 16 |
| llama3.2:3b | ru | link | duplicate_name minus baseline | -75.0 | [-100.0, -37.5] | 8 |
| llama3.2:3b | ru | link | generic_name minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| llama3.2:3b | ru | link | img_no_alt minus baseline | -75.0 | [-100.0, -37.5] | 8 |
| llama3.2:3b | ru | link | span_not_link minus baseline | -12.5 | [-37.5, +0.0] | 8 |
| llama3.2:3b | ru | textbox | label_not_linked minus baseline | -12.5 | [-37.5, +0.0] | 8 |
| llama3.2:3b | ru | textbox | no_label minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| llama3.2:3b | ru | textbox | placeholder_only minus baseline | -12.5 | [-37.5, +0.0] | 8 |
| mistral:7b | en | button | div_not_button minus baseline | +0.0 | [+0.0, +0.0] | 16 |
| mistral:7b | en | button | duplicate_name minus baseline | -31.2 | [-56.2, -12.5] | 16 |
| mistral:7b | en | button | generic_name minus baseline | -81.2 | [-100.0, -62.5] | 16 |
| mistral:7b | en | button | icon_no_name minus baseline | -100.0 | [-100.0, -100.0] | 16 |
| mistral:7b | en | button | img_no_alt minus baseline | -100.0 | [-100.0, -100.0] | 16 |
| mistral:7b | en | link | duplicate_name minus baseline | -62.5 | [-100.0, -25.0] | 8 |
| mistral:7b | en | link | generic_name minus baseline | -100.0 | [-100.0, -100.0] | 8 |
| mistral:7b | en | link | img_no_alt minus baseline | -100.0 | [-100.0, -100.0] | 8 |
| mistral:7b | en | link | span_not_link minus baseline | -12.5 | [-37.5, +0.0] | 8 |
| mistral:7b | en | textbox | label_not_linked minus baseline | -12.5 | [-37.5, +0.0] | 8 |
| mistral:7b | en | textbox | no_label minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| mistral:7b | en | textbox | placeholder_only minus baseline | +0.0 | [+0.0, +0.0] | 8 |
| mistral:7b | ru | button | div_not_button minus baseline | +0.0 | [+0.0, +0.0] | 16 |
| mistral:7b | ru | button | duplicate_name minus baseline | -37.5 | [-62.5, -12.5] | 16 |
| mistral:7b | ru | button | generic_name minus baseline | -75.0 | [-93.8, -56.2] | 16 |
| mistral:7b | ru | button | icon_no_name minus baseline | -93.8 | [-100.0, -81.2] | 16 |
| mistral:7b | ru | button | img_no_alt minus baseline | -93.8 | [-100.0, -81.2] | 16 |
| mistral:7b | ru | link | duplicate_name minus baseline | -37.5 | [-75.0, -12.5] | 8 |
| mistral:7b | ru | link | generic_name minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| mistral:7b | ru | link | img_no_alt minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| mistral:7b | ru | link | span_not_link minus baseline | -12.5 | [-37.5, +0.0] | 8 |
| mistral:7b | ru | textbox | label_not_linked minus baseline | -12.5 | [-37.5, +0.0] | 8 |
| mistral:7b | ru | textbox | no_label minus baseline | -75.0 | [-100.0, -50.0] | 8 |
| mistral:7b | ru | textbox | placeholder_only minus baseline | -12.5 | [-37.5, +0.0] | 8 |
| qwen2.5:3b | en | button | div_not_button minus baseline | -6.2 | [-18.8, +0.0] | 16 |
| qwen2.5:3b | en | button | duplicate_name minus baseline | -37.5 | [-62.5, -12.5] | 16 |
| qwen2.5:3b | en | button | generic_name minus baseline | -93.8 | [-100.0, -81.2] | 16 |
| qwen2.5:3b | en | button | icon_no_name minus baseline | -100.0 | [-100.0, -100.0] | 16 |
| qwen2.5:3b | en | button | img_no_alt minus baseline | -87.5 | [-100.0, -68.8] | 16 |
| qwen2.5:3b | en | link | duplicate_name minus baseline | -75.0 | [-100.0, -37.5] | 8 |
| qwen2.5:3b | en | link | generic_name minus baseline | -100.0 | [-100.0, -100.0] | 8 |
| qwen2.5:3b | en | link | img_no_alt minus baseline | -100.0 | [-100.0, -100.0] | 8 |
| qwen2.5:3b | en | link | span_not_link minus baseline | -25.0 | [-62.5, +0.0] | 8 |
| qwen2.5:3b | en | textbox | label_not_linked minus baseline | -25.0 | [-62.5, +25.0] | 8 |
| qwen2.5:3b | en | textbox | no_label minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| qwen2.5:3b | en | textbox | placeholder_only minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| qwen2.5:3b | ru | button | div_not_button minus baseline | +6.2 | [+0.0, +18.8] | 16 |
| qwen2.5:3b | ru | button | duplicate_name minus baseline | -43.8 | [-68.8, -12.5] | 16 |
| qwen2.5:3b | ru | button | generic_name minus baseline | -75.0 | [-93.8, -50.0] | 16 |
| qwen2.5:3b | ru | button | icon_no_name minus baseline | -93.8 | [-100.0, -81.2] | 16 |
| qwen2.5:3b | ru | button | img_no_alt minus baseline | -93.8 | [-100.0, -81.2] | 16 |
| qwen2.5:3b | ru | link | duplicate_name minus baseline | -50.0 | [-87.5, -12.5] | 8 |
| qwen2.5:3b | ru | link | generic_name minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| qwen2.5:3b | ru | link | img_no_alt minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| qwen2.5:3b | ru | link | span_not_link minus baseline | +12.5 | [-25.0, +50.0] | 8 |
| qwen2.5:3b | ru | textbox | label_not_linked minus baseline | -37.5 | [-75.0, -12.5] | 8 |
| qwen2.5:3b | ru | textbox | no_label minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| qwen2.5:3b | ru | textbox | placeholder_only minus baseline | -50.0 | [-87.5, -12.5] | 8 |
| qwen2.5:7b | en | button | div_not_button minus baseline | +0.0 | [+0.0, +0.0] | 16 |
| qwen2.5:7b | en | button | duplicate_name minus baseline | -31.2 | [-56.2, -12.5] | 16 |
| qwen2.5:7b | en | button | generic_name minus baseline | -56.2 | [-81.2, -31.2] | 16 |
| qwen2.5:7b | en | button | icon_no_name minus baseline | -100.0 | [-100.0, -100.0] | 16 |
| qwen2.5:7b | en | button | img_no_alt minus baseline | -100.0 | [-100.0, -100.0] | 16 |
| qwen2.5:7b | en | link | duplicate_name minus baseline | -25.0 | [-62.5, +0.0] | 8 |
| qwen2.5:7b | en | link | generic_name minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| qwen2.5:7b | en | link | img_no_alt minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| qwen2.5:7b | en | link | span_not_link minus baseline | -12.5 | [-37.5, +0.0] | 8 |
| qwen2.5:7b | en | textbox | label_not_linked minus baseline | +0.0 | [+0.0, +0.0] | 8 |
| qwen2.5:7b | en | textbox | no_label minus baseline | -87.5 | [-100.0, -62.5] | 8 |
| qwen2.5:7b | en | textbox | placeholder_only minus baseline | +0.0 | [+0.0, +0.0] | 8 |
| qwen2.5:7b | ru | button | div_not_button minus baseline | +0.0 | [+0.0, +0.0] | 16 |
| qwen2.5:7b | ru | button | duplicate_name minus baseline | -12.5 | [-31.2, +0.0] | 16 |
| qwen2.5:7b | ru | button | generic_name minus baseline | -62.5 | [-87.5, -37.5] | 16 |
| qwen2.5:7b | ru | button | icon_no_name minus baseline | -100.0 | [-100.0, -100.0] | 16 |
| qwen2.5:7b | ru | button | img_no_alt minus baseline | -100.0 | [-100.0, -100.0] | 16 |
| qwen2.5:7b | ru | link | duplicate_name minus baseline | -25.0 | [-62.5, +0.0] | 8 |
| qwen2.5:7b | ru | link | generic_name minus baseline | -75.0 | [-100.0, -37.5] | 8 |
| qwen2.5:7b | ru | link | img_no_alt minus baseline | -75.0 | [-100.0, -37.5] | 8 |
| qwen2.5:7b | ru | link | span_not_link minus baseline | -12.5 | [-50.0, +37.5] | 8 |
| qwen2.5:7b | ru | textbox | label_not_linked minus baseline | +0.0 | [+0.0, +0.0] | 8 |
| qwen2.5:7b | ru | textbox | no_label minus baseline | -62.5 | [-87.5, -25.0] | 8 |
| qwen2.5:7b | ru | textbox | placeholder_only minus baseline | +0.0 | [+0.0, +0.0] | 8 |
| llama3.1:8b | both | button | Roman Urdu minus English | -6.2 | [-12.5, +0.0] | 96 |
| llama3.1:8b | both | link | Roman Urdu minus English | +2.5 | [+0.0, +7.5] | 40 |
| llama3.1:8b | both | textbox | Roman Urdu minus English | +12.5 | [+3.1, +25.0] | 32 |
| llama3.2:3b | both | button | Roman Urdu minus English | -14.6 | [-22.9, -7.3] | 96 |
| llama3.2:3b | both | link | Roman Urdu minus English | -5.0 | [-17.5, +10.0] | 40 |
| llama3.2:3b | both | textbox | Roman Urdu minus English | -6.2 | [-21.9, +9.4] | 32 |
| mistral:7b | both | button | Roman Urdu minus English | -4.2 | [-9.4, +0.0] | 96 |
| mistral:7b | both | link | Roman Urdu minus English | -17.5 | [-30.0, -7.5] | 40 |
| mistral:7b | both | textbox | Roman Urdu minus English | +0.0 | [-9.4, +9.4] | 32 |
| qwen2.5:3b | both | button | Roman Urdu minus English | -2.1 | [-8.3, +4.2] | 96 |
| qwen2.5:3b | both | link | Roman Urdu minus English | -10.0 | [-20.0, -2.5] | 40 |
| qwen2.5:3b | both | textbox | Roman Urdu minus English | +0.0 | [-9.4, +9.4] | 32 |
| qwen2.5:7b | both | button | Roman Urdu minus English | +2.1 | [-3.1, +7.3] | 96 |
| qwen2.5:7b | both | link | Roman Urdu minus English | -7.5 | [-17.5, +0.0] | 40 |
| qwen2.5:7b | both | textbox | Roman Urdu minus English | +6.2 | [+0.0, +15.6] | 32 |

## Exact role-and-name locator (the v0.2.0 script rule)

| Element | Defect | Success | Pages |
|---|---|---|---|
| button | baseline | 100% | 16 |
| button | div_not_button | 0% | 16 |
| button | duplicate_name | 0% | 16 |
| button | generic_name | 0% | 16 |
| button | icon_no_name | 0% | 16 |
| button | img_no_alt | 0% | 16 |
| link | baseline | 100% | 8 |
| link | duplicate_name | 0% | 8 |
| link | generic_name | 0% | 8 |
| link | img_no_alt | 0% | 8 |
| link | span_not_link | 0% | 8 |
| textbox | baseline | 100% | 8 |
| textbox | label_not_linked | 0% | 8 |
| textbox | no_label | 0% | 8 |
| textbox | placeholder_only | 100% | 8 |
