from sys import stdin

pHP, pATK, mHP, mATK = map(int, stdin.readline().split())
sk_HP, sk_Heal = map(int, stdin.readline().split())

mHP = mHP + sk_Heal if sk_HP >= pATK or ((mHP%pATK) != 0 and (mHP%pATK) <= sk_HP) else mHP
p_atkCount = int(mHP / pATK) if mHP%pATK == 0 else int(mHP / pATK)+1
m_atkCount = int(pHP / mATK) if pHP%mATK == 0 else int(pHP / mATK)+1

if p_atkCount <= m_atkCount: print("Victory!")
elif p_atkCount > m_atkCount: print("gg")
  