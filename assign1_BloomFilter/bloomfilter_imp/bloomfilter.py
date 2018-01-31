import mmh3
import sys
import hashlib

bf_num = 10000000

class BloomFilter:
    def __init__(self):
        self.bucket_num = bf_num
        self.buckets = [0] * bf_num
        self.buckets_five = [0] * bf_num
    
    def add_three(self, insert_str):
        first_hash = int(mmh3.hash(insert_str)) % self.bucket_num

        second_hash = int(hashlib.md5(insert_str).hexdigest(), 16) % self.bucket_num

        third_hash = int(hashlib.sha1(insert_str).hexdigest(), 16) % self.bucket_num

        self.buckets[first_hash] = 1
        self.buckets[second_hash] = 1
        self.buckets[third_hash] = 1

        self.buckets_five[first_hash] = 1
        self.buckets_five[second_hash] = 1
        self.buckets_five[third_hash] = 1

    def add_five(self, insert_str):
        fourth_hash = int(hashlib.sha512(insert_str).hexdigest(), 16) % self.bucket_num
        fifth_hash = int(hashlib.sha256(insert_str).hexdigest(), 16) % self.bucket_num

        self.buckets_five[fourth_hash] = 1
        self.buckets_five[fifth_hash] = 1

    def filter_three(self, n_input, output_3):
        with open(n_input, 'r') as in_file:
            with open(output_3, 'w') as out_file:
                for line in in_file:
                    line = str(line.rstrip())
                    first_hash = mmh3.hash(line) % self.bucket_num
                    second_hash = int(hashlib.md5(line).hexdigest(), 16) % self.bucket_num
                    third_hash = int(hashlib.sha1(line).hexdigest(), 16) % self.bucket_num

                    if (self.buckets[first_hash] + self.buckets[second_hash] + self.buckets[third_hash]) == 3:
                        out_file.write("maybe\n")
                    else:
                        out_file.write("no\n")

    def filter_five(self, n_input, output_5):
        with open(n_input, 'r') as in_file:
            with open(output_5, 'w') as out_file:
                for line in in_file:
                    line = str(line.rstrip())
                    first_hash = mmh3.hash(line) % self.bucket_num
                    second_hash = int(hashlib.md5(line).hexdigest(), 16) % self.bucket_num
                    third_hash = int(hashlib.sha1(line).hexdigest(), 16) % self.bucket_num
                    fourth_hash = int(hashlib.sha512(line).hexdigest(), 16) % self.bucket_num
                    fifth_hash = int(hashlib.sha256(line).hexdigest(), 16) % self.bucket_num

                    if (self.buckets_five[first_hash] + self.buckets_five[second_hash] + self.buckets_five[third_hash] + self.buckets_five[fourth_hash] + self.buckets_five[fifth_hash]) == 5:
                        out_file.write("maybe\n")
                    else:
                        out_file.write("no\n")
    
        
def main():
    # file arguments
    # /bloomfilter.py -d dictionary.txt -i input.txt -o output3.txt output5.txt
    if len(sys.argv) == 8 and sys.argv[1] == '-d' and sys.argv[3] == '-i' and sys.argv[5] == '-o':
        n_dictionary = str(sys.argv[2])
        n_input = str(sys.argv[4])
        output_3 = str(sys.argv[6])
        output_5 = str(sys.argv[7])
        bf = BloomFilter()

        with open(n_dictionary, 'r') as fobj:
            for line in fobj:
                str_line = str(line.rstrip())
                bf.add_three(str_line)
                bf.add_five(str_line)

        bf.filter_three(n_input, output_3)
        bf.filter_five(n_input, output_5)
            
    else:
        print "Usage: python bloomfilter.py -d dictionary.txt -i input.txt -o output3.txt output5.txt" 
        return 1

if __name__ == "__main__":
    main()
