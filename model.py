import google.generativeai as palm
palm.configure(api_key="YOUR API KEY")

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}
input = ''
prompt = f"""input: Once upon a time there was... 
output: a happy princess who lived in a kingdom of Goblins
input: And then... 
output: the warriors of the South invaded the Land of the West
input: So... 
output: We can't usurp thrones like Sir Lancelot did
input: I've never...
output: seen killer rabbits
input: {input}
output:"""

response = palm.generate_text(
  **defaults,
  prompt=prompt
)
print(response.result)
