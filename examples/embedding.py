from groq import Groq

client = Groq()

embedding = client.embeddings.create(
    #
    # Required parameters
    #
    # The input texts to embed.
    input=["hello world"],
    # The model to use.
    model="nomic-embed-text-v1.5",
    #
    # Optional parameters
    #
    # Format to return the embeddings in.
    # Only "float" is supported at the moment.
    encoding_format="float",
    # A unique identifier representing your end-user.
    user="user",
)

print(embedding)
