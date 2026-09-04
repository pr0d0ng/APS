from decimal import Decimal, ROUND_DOWN

A, B = map(int, input().split())

result = Decimal(A) / Decimal(B)

print(result.quantize(Decimal('1e-20'), rounding=ROUND_DOWN))