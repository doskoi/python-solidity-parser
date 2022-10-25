import os
import unittest
from multiprocessing import Pool
from typing import Tuple

from solidity_parser.parser import parse, objectify


def parse_test(param: Tuple[str, str]):
    address, text = param
    print(address + " start")
    try:
        kk = parse(text=text, loc=True)
        kk2 = objectify(kk)
        if kk2 is not None:
            print(address + " ok")
            file = r'tmp/check.txt'
            with open(file, 'a+') as f:
                f.write(address+"\n")
        else:
            print(address + " is none")
    except Exception as e:
        print(address + " e rr")
        raise e


class MyTestCase(unittest.TestCase):

    def test_something(self):
        path = "/mnt/work/code/GongSI/lskj/Background_Project/chain_monitoring/tmp/test_contract"

        dir = "0xA8D5DFcf36bCb29adF9EBbD753c2978B9a982cC6"

        for files in os.listdir(path + "/" + dir):
            f = open(path + "/" + dir + "/" + files)
            contract_body = f.read()
            f.close()

            (file_name, ext) = os.path.splitext(files)

            kk = parse(text=contract_body, loc=True)
            kk2 = objectify(kk)
            # storage_info = get_storage_info(kk2, contract_name, insert_node)
            # kk = calculate_storage_key((contract_body, file_name, False))
            print(kk2)

    def test_from_file_pool(self):
        """
        批量测试文件语法解析
        :return:
        """
        path = "/mnt/work/code/GongSI/lskj/Background_Project/chain_monitoring/tmp/test_contract"

        pool = Pool(processes=16)  # 默认线程数为16

        set_vul = list()

        for dir in os.listdir(path):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
            # print("files", dir)

            for files in os.listdir(path + "/" + dir):
                f = open(path + "/" + dir + "/" + files)
                contract_body = f.read()
                f.close()
                (file_name, ext) = os.path.splitext(files)
                set_vul.append((dir, contract_body))

        # 创建线程池，其返回值vul_lists就是扫描结果，vul_lists为一个双层嵌套的list，每一个文件扫描到的漏洞组成一个list，每个文件文件的list组成vul_list
        vul_lists = pool.map(
            parse_test,
            set_vul
        )
        # 等待所有线程完成
        pool.close()
        pool.join()
        # self.assertEqual(True, False)  # add assertion here

    def test_from_file(self):
        """
        批量测试文件语法解析
        :return:
        """
        path = "/mnt/work/code/GongSI/lskj/Background_Project/chain_monitoring/tmp/test_contract"


        for dir in os.listdir(path):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
            # print("files", dir)

            for files in os.listdir(path + "/" + dir):
                f = open(path + "/" + dir + "/" + files)
                contract_body = f.read()
                f.close()
                (file_name, ext) = os.path.splitext(files)

                if os.path.exists('tmp/check.txt'):
                    f_2 = open('tmp/check.txt')
                    check_list = f_2.read()
                    f_2.close()
                    if dir not in check_list:
                        parse_test((dir, contract_body))
                else:
                    parse_test((dir, contract_body))
        # self.assertEqual(True, False)  # add assertion here



if __name__ == '__main__':
    unittest.main()
