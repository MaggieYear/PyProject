# -*- coding: utf-8 -*-
import time
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import os

class XmlUtils:

    def __init__(self):
        pass

    def read_xml(self,in_path):
        """读取并解析xml文件
        in_path: xml路径
        return: tree"""
        tree = ET.parse(in_path)
        return tree

    def creat_dict(self,root):
        """xml生成为dict：，
        将tree中个节点添加到list中，将list转换为字典dict_init
        叠加生成多层字典dict_new"""
        dict_new = {}
        for key, valu in enumerate(root):
            dict_init = {}
            list_init = []
            for item in valu:
                list_init.append([item.tag, item.text])
                for lists in list_init:
                    dict_init[lists[0]] = lists[1]
                    dict_new[key] = dict_init
        return dict_new

    """
    <?xml version='1.0' encoding='utf-8'?>
    <baspools>
    
    <bas>
    <basprovider>0</basprovider>
    <portal_version>1</portal_version>
    <timeout>111</timeout>
    <retry>111</retry>
    <auth_type>111</auth_type>
    </bas>
    
    <bas>
    <basprovider>0</basprovider>
    <portal_version>1</portal_version>
    <timeout>5000</timeout>
    <retry>3</retry>
    <auth_type>0</auth_type>
    </bas>
    
    </baspools>
    
    """
    def dict_to_xml(self,input_dict, root_tag, node_tag):
        """ 定义根节点root_tag，定义第二层节点node_tag
        第三层中将字典中键值对对应参数名和值
        return: xml的tree结构 """
        root_name = ET.Element(root_tag)
        for (k, v) in input_dict.items():
            node_name = ET.SubElement(root_name, node_tag)
            for key, val in v.items():
                key = ET.SubElement(node_name, key)
                key.text = val
        return root_name


    """
    <url>
        <loc>http://www.uedsc.com/tag/net</loc>
        <lastmod>2015-02-27T01:12:09+00:00</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.3</priority>
    </url>
    <url>
        <loc>http://www.uedsc.com/tag/%e9%bd%bf%e8%bd%ae%e5%9b%be%e6%a0%87</loc>
        <lastmod>2014-08-08T01:10:39+00:00</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.3</priority>
    </url>
    """
    def urlmap_to_xml(self,input_dict,root_tag,node_tag):
        """ 定义根节点root_tag，定义第二层节点node_tag
        第三层中将字典中键值对对应参数名和值
        return: xml的tree结构 """
        #root_name = ET.Element(node_tag)

        root_name = ET.Element(root_tag)
        for (k, v) in input_dict.items():
            node_name = ET.Element(node_tag)
            root_name.append(node_name)
            #node_name = ET.SubElement(root_name, node_tag)
            for (key, val) in sorted(v.items(), key=lambda e: e[0], reverse=True):
                key = ET.SubElement(node_name, key)
                key.text = val
        return root_name

    def out_xml(self,root,path,filename):

        if not os.path.exists(path):
            os.makedirs(path)
        file_path = path + '/' + filename

        """格式化root转换为xml文件"""
        rough_string = ET.tostring(root, 'utf-8')
        reared_content = minidom.parseString(rough_string)

        with open(file_path, 'w+') as fs:
            reared_content.writexml(fs, addindent=" ", newl="\n", encoding="utf-8")
        return True

if __name__ == '__main__':
    start = time.clock()  # 记录处理开始时间；与最后一行一起使用，来判断输出运行时间。

    in_files = r"url_xml\baspool_read.xml"
    out_file = r"url_xml\baspool_out.xml"

    xmlUtils = XmlUtils()
    tree = xmlUtils.read_xml(in_files)
    node_new = xmlUtils.creat_dict(tree.getroot()) # 将xml转换为dict
    root = xmlUtils.dict_to_xml(node_new, "baspools", "bas") # 将dict转换为xml
    xmlUtils.out_xml(root,out_file) # 输出xml到out_files

    end = time.clock()
    print("read: %f s" % (end - start))
