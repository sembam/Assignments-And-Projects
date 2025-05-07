f = open('lorem-ipsum.txt', 'w')
f.write('\n Lorem ipsum dolor sit amet. Qui voluptas exercitationem eos aliquam ipsum in nisi itaque et aliquid mollitia ut blanditiis praesentium vel deserunt labore est doloribus nisi. Qui placeat totam ab corrupti maiores ut numquam nostrum qui nisi sint. Non dolor enim eum fuga commodi ad quibusdam sunt et beatae animi. Ut harum optio ut libero iste est sint dicta vel nulla animi ut dolores dolores qui rerum aliquam.')
f.close()

with open('lorem-ipsum.txt', 'r') as f:
    txt1 = f.read()

f = open('lorem-ipsum-copy.txt', 'w')
f.write('\n \n Egestas accumsan senectus taciti tristique sem. Amet convallis sem finibus faucibus ullamcorper. Mauris consequat gravida dolor odio sed tempor lobortis. Per pretium pretium aenean platea torquent metus. Nec placerat efficitur class habitasse aliquet. Finibus nam commodo sodales potenti amet parturient. Pulvinar hendrerit enim, finibus penatibus dignissim metus nostra praesent. Cubilia neque ultrices consequat suscipit id. Turpis penatibus molestie dolor habitant ullamcorper dis?')
f.close()

with open('lorem-ipsum-copy.txt', 'r') as x:
    txt2 = x.read()
    
print(txt1, txt2)