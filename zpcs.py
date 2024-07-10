import zhipuai
zhipuai.api_key = "457e3a55c2035be3869a49e1ce5cba74.oARHiQyMbiR0UJCz"
from zhipuai_llm import ZhipuAILLM
zhipuai_model = ZhipuAILLM(model="chatglm_std", temperature=0, zhipuai_api_key= zhipuai.api_key)
print(zhipuai_model.generate(['你好']))
