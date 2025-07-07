import asyncio
from revoltutils import EncodingUtils

async def test_encoding_utils():
    text = "hello"
    binary_data = b"hello"
    xor_key = "key"

    print("[*] Base64 Encode:", await EncodingUtils.base64_encode(text))
    print("[*] Base64 Decode:", await EncodingUtils.base64_decode(await EncodingUtils.base64_encode(text)))

    print("[*] Base32 Encode:", await EncodingUtils.base32_encode(text))
    print("[*] Base32 Decode:", await EncodingUtils.base32_decode(await EncodingUtils.base32_encode(text)))

    print("[*] Hex Encode:", await EncodingUtils.hex_encode(text))
    print("[*] Hex Decode:", await EncodingUtils.hex_decode(await EncodingUtils.hex_encode(text)))

    print("[*] URL Encode:", await EncodingUtils.url_encode(text))
    print("[*] URL Decode:", await EncodingUtils.url_decode(await EncodingUtils.url_encode(text)))

    print("[*] ROT13:", await EncodingUtils.rot13(text))

    print("[*] XOR Encode:", await EncodingUtils.xor_encode(text, xor_key))
    print("[*] XOR Bytes:", (await EncodingUtils.xor_bytes(binary_data, xor_key.encode())).decode(errors='ignore'))

    print("[*] MD5 Hash:", await EncodingUtils.hash_md5(text))
    print("[*] SHA1 Hash:", await EncodingUtils.hash_sha1(text))
    print("[*] SHA256 Hash:", await EncodingUtils.hash_sha256(text))
    print("[*] SHA512 Hash:", await EncodingUtils.hash_sha512(text))

    padded = await EncodingUtils.pad_string(text, block_size=10)
    print("[*] Padded Text:", repr(padded))

    binary = await EncodingUtils.string_to_binary(text)
    print("[*] String to Binary:", binary)
    print("[*] Binary to String:", await EncodingUtils.binary_to_string(binary))

    morse = await EncodingUtils.to_morse(text)
    print("[*] Morse Code:", morse)
    print("[*] From Morse Code:", await EncodingUtils.from_morse(morse))


if __name__ == "__main__":
    asyncio.run(test_encoding_utils())
