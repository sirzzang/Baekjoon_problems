sugar = int(input())

fiveCount = sugar//5              # 초기 5키로 배달횟수 : 5로 나눈 몫
sugar = sugar % 5                 
threeCount = 0

while fiveCount >= 0:             # 3의 배수일 수도 있으니까 0 이상일 때로 지정해줘야 함.
    if sugar % 3 == 0:            # 남은 설탕이 0이거나 3의 배수일 때
        threeCount = sugar // 3   # 3배달횟수는 남은 설탕을 3으로 나눈 몫
        sugar = sugar % 3         # 남은 설탕이 0인지 확인하기 위해 sugar 초기화
        break
    fiveCount -= 1                # 아니면 5키로 배달횟수 줄이고
    sugar += 5                    # 남은 설탕에 5키로 더해줘라

print((fiveCount + threeCount) if sugar == 0 else -1)

# 이 과정 반복해서 남은 설탕이 0이면 더한 배달횟수 출력하고, 아니면 -1이다.
 

# # 최종 이전 연습

# # numList = list(range(3, 501))
# # howList = []
# # for num in numList:
# #     if str(num)[-1] in ["5", "0"]:
# #         print(num, num//5, "5의 배수") # 최소 배달 횟수
# #     elif str(num)[-1] in ["3","6","9"]:
# #        print(num, (num-num%10)//5+(num%10)//3, "10의배수+3,6,9") #일의자리 3의배수값 + 10의배수는 5로 나눠주기
# #     else: # 나머지가 문제다
# #         print(num)
# #         howList.append(num)
# # print(howList)

# howList = [4, 7, 8, 11, 12, 14, 17, 18, 21, 22, 24, 27, 28, 31, 32, 34, 37, 38, 41, 42, 44, 47, 48, 51, 52, 54, 57, 58, 61, 62, 64, 67, 68, 71, 72, 74, 77, 78, 81, 82, 84, 87, 88, 91, 92, 94, 97, 98, 101, 102, 104, 107, 108, 111, 112, 114, 117, 118, 121, 122, 124, 127, 128, 131, 132, 134, 137, 138, 141, 142, 144, 147, 148, 151, 152, 154, 157, 158, 161, 162, 164, 167, 168, 171, 172, 174, 177, 178, 181, 182, 184, 187, 188, 191, 192, 194, 197, 198, 201, 202, 204, 207, 208, 211, 212, 214, 217, 218, 221, 222, 224, 227, 228, 231, 232, 234, 237, 238, 241, 242, 244, 247, 248,
# 251, 252, 254, 257, 258, 261, 262, 264, 267, 268, 271, 272, 274, 277, 278, 281, 282, 284, 287, 288, 291, 292, 294, 297, 298, 301, 302, 304, 307, 308, 311, 312, 314, 317, 318, 321, 322, 324, 327, 328, 331, 332, 334, 337, 338, 341, 342, 344, 347, 348, 351, 352, 354, 357, 358, 361, 362, 364, 367, 368, 371, 372, 374, 377, 378, 381, 382, 384, 387, 388, 391, 392, 394, 397, 398, 401, 402, 404, 407, 408, 411, 412, 414, 417, 418, 421, 422, 424, 427, 428, 431, 432, 434, 437, 438, 441, 442, 444, 447, 448, 451, 452, 454, 457, 458, 461, 462, 464, 467, 468, 471, 472, 474,
# 477, 478, 481, 482, 484, 487, 488, 491, 492, 494, 497, 498]

# for how in howList:
#     n = 0
#     while how > 0:
#         how -= 3
#         if how - 3 < 0:
#             n = -1
#             break
#         elif how % 5 == 0:
#             n = (how // 5)
#         elif how % 3 != 0 and how % 5 != 0:
#             n = -1

# print(how, n)



# # for how in howList:
# #     if (how % 15) % 3 == 0:
# #         print(how, (how - (how % 15)) // 5 + (how % 15) //3, "howList 중 15로 나눈 나머지 3의 배수")
# #     else: # 이제 남는 애들은 그냥 5로 계속 뺼 수밖에 없다.
# #         print(how, how // 15, how % 15)

# # 아래 방법 사용하면 18일 때가 문제가 됐다. 따라서! 5의 배수 남을때까지 3을 빼주기로!
# # # x가 주어졌을 때
# # # 그걸 5로 계속 뺀다
# # # 5로 뺀 후의 결과가 3의 배수이거나 0이면 멈춘다
# # # 0이면 그 때까지의 횟수 return
# # # 2나 1이면 -1
# # # 3의 배수면 3으로 나눈 몫 + 그 때까지의 횟수 return.

# # # def hello(count):

# # #     n = 0

# # #     while True:
# # #         if count % 3 != 0:
# # #             n += 1
# # #             count -= 5

# # #         else:
# # #             break
# # #         print(count)
# # #     print(n)


# # #     print(count//3)
    

# # # hello(12)


# # # def hello(count):

# # #     n = 0

# # #     while True:
# # #         if count % 3 != 0:
# # #             n += 1
# # #             count -= 5

# # #         else:
# # #             break
# # #         print(count)
# # #     print(n)


# # #     print(count//3)
    

# # # hello(12)

# # # 이렇게 짜면 18의 경우가 문제가 됨. 3의 배수니까...

# # user_input = int(input())


# # if user_input % 5 == 0:
# #     print(user_input // 5)

# # else:

# #     n = 1
# #     user_input = user_input - 5
    
# #     while user_input % 3 != 0 and user_input // 3 <= 4 :
# #         n += 1
# #         user_input -= 5
# #         if user_input % 3 == 0:
# #             break

# #     if user_input > 0 :
# #         print((user_input // 3) + n)

# #     else :
# #         print(-1)  