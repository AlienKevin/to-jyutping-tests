import re

cjk_pattern = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002ebef\U00030000-\U000323af\ufa0e\ufa0f\ufa11\ufa13\ufa14\ufa1f\ufa21\ufa23\ufa24\ufa27\ufa28\ufa29\u3006\u3007]')
punc_dict = dict(
	zip(
		'''!"'(),-./:;?[]{}~·‐‑‒–—―‘’“”…⋮⋯⸱⸳⸺⸻、。〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟・︐︑︒︓︔︕︖︗︘︙︱︲︵︶︷︸︹︺︻︼︽︾︿﹀﹁﹂﹃﹄﹇﹈﹐﹑﹒﹔﹕﹖﹗﹘﹙﹚﹛﹜﹝﹞﹣！＂＇（），－．／：；？［］｛｝～｟｠｡｢｣､･''',
		'''!"'(),-./:;?[]{}~·------‘’“”………··--,.‘’“”“”‘’[][][][][]~“””·,,.:;!?[]…--(){}[][]“”‘’“”‘’[],,.;:?!-(){}[]-!"'(),-./:;?[]{}~().“”,·'''
	)
)
punc_pattern = re.compile(f"[{''.join(re.escape(c) for c in punc_dict.keys())}]")

filtered_lines = []

with open("jyutping_sentences.txt", "r") as f:
    lines = [line for line in f.readlines() if len(line.strip()) > 0]
    for i in range(0, len(lines), 2):
        yue = lines[i].strip()
        if len(yue) < 5:
            continue
        jyutping = lines[i + 1].strip()
        # check all characters are CJK characters or punctuations
        if all([cjk_pattern.match(char) or punc_pattern.match(char) for char in yue]):
            filtered_lines.append((punc_pattern.sub(" ", yue).strip(), jyutping))

with open("jyutping_sentences_filtered.txt", "w") as f:
    for (sentence, prs) in filtered_lines:
        f.write(sentence + "\n")
        f.write(prs + "\n\n")
