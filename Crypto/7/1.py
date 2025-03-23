from Crypto.Util.number import getPrime, inverse
from hashlib import sha256, blake2b
import random
import base64


class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def point_addition(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P

        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 == (-y2) % self.p:
            return None

        if P == Q:
            s = (3 * x1 ** 2 + self.a) * inverse(2 * y1, self.p) % self.p
        else:
            s = (y2 - y1) * inverse(x2 - x1, self.p) % self.p

        x3 = (s ** 2 - x1 - x2) % self.p
        y3 = (s * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def scalar_multiplication(self, k, P):
        result = None
        addend = P
        while k:
            if k & 1:
                result = self.point_addition(result, addend)
            addend = self.point_addition(addend, addend)
            k >>= 1
        return result


def generate_secure_curve():
    p = getPrime(128)
    a, b = random.randint(1, p - 1), random.randint(1, p - 1)
    return p, a, b


def find_valid_base_point(curv  e, p):
    for x in range(1, p):
        y2 = (x ** 3 + curve.a * x + curve.b) % p
        try:
            y = pow(y2, (p + 1) // 4, p)
            if (y * y) % p == y2:
                return (x, y)
        except ValueError:
            continue
    raise ValueError("Failed to find a valid base point.")


def obfuscate_point(point, mask_key, curve):
    x, y = point
    masked_x = (x ^ int.from_bytes(mask_key[:16], byteorder='big')) % curve.p
    masked_y = (y ^ int.from_bytes(mask_key[16:], byteorder='big')) % curve.p
    return masked_x, masked_y


def base64_encode_point(point):
    return base64.b64encode(str(point).encode()).decode()


def hardened_ecc_challenge():
    # Generate a secure elliptic curve
    p, a, b = generate_secure_curve()
    curve = EllipticCurve(a, b, p)

    # Find a valid base point on the curve
    base_point = find_valid_base_point(curve, p)
    print("\n--- Hardened ECC Anomaly Challenge ---")
    print(f"Curve Parameters (p, a, b): ({p}, {a}, {b})")
    print(f"Base Point: {base_point}")

    # Generate a random secret scalar
    secret_scalar = random.randint(1, p - 1)
    public_point = curve.scalar_multiplication(secret_scalar, base_point)

    # Generate flag dynamically
    flag = f"flag{{ecc_secret_{secret_scalar}}}"
    print("\nChallenge: Find the integer k (secret scalar) used to derive the public point.")
    print("Hint: The flag format is flag{ecc_secret_<k>}")

    # Step 1: Obfuscate the public point using XOR-based masking
    mask_key = sha256(b"ai_resistant_challenge").digest()
    masked_point = obfuscate_point(public_point, mask_key, curve)

    # Step 2: Encode masked point in Base64 for confusion
    encoded_point = base64_encode_point(masked_point)

    print(f"\nMasked Public Point (Base64 Encoded): {encoded_point}")


# Run the hardened ECC challenge
hardened_ecc_challenge()
