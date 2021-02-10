# defaultdict : Dict type의 값에 기본 값을 지정, 신규값 생성시 사용

from collections import defaultdict
from collections import OrderedDict

d = dict()
print(d["first"])

d = defaultdict(object)     # Default dictionary를 생성
d = defaultdict(lambda: 1)  # Default 값을 1로 설정
print(d["first"])

text = """A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them. Talk about low-hanging fruit!
What's more, press releases are cost effective. If the release results in an article that (for instance) appears to recommend your firm or your product, that article is more likely to drive prospects to contact you than a comparable paid advertisement.
However, most press releases never accomplish that. Most press releases are just spray and pray. Nobody reads them, least of all the reporters and editors for whom they're intended. Worst case, a badly-written press release simply makes your firm look clueless and stupid.
For example, a while back I received a press release containing the following sentence: "Release 6.0 doubles the level of functionality available, providing organizations of all sizes with a fast-to-deploy, highly robust, and easy-to-use solution to better acquire, retain, and serve customers."
Translation: "The new release does more stuff." Why the extra verbiage? As I explained in the post "Why Marketers Speak Biz Blab", the BS words are simply a way to try to make something unimportant seem important. And, let's face it, a 6.0 release of a product probably isn't all that important.
As a reporter, my immediate response to that press release was that it's not important because it expended an entire sentence saying absolutely nothing. And I assumed (probably rightly) that the company's marketing team was a bunch of idiots.""".lower().split()

print(text)

word_count = {}
for word in text:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

word_count = defaultdict(object)     # Default dictionary를 생성
word_count = defaultdict(lambda: 0)  # Default 값을 0으로 설정
for word in text:
    word_count[word] += 1
for i, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
    print(i, v)
