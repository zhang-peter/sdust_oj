#!/usr/bin/python
# encoding=utf8

pending = 11
keyword_check_ok = 123
compile_ok = 133
run_ok = 143
output_check_ok = 153


keyword_checking = 122
compiling = 132
running = 142
output_checking = 155

keyword_checked_error = 21
compiled_error = 22
runtime_error = 23
memory_over_error = 24
presentation_error = 25
wrong_answer = 26

fetched = 0
accept = 10000

STATUS_WORD = {
        pending : u"等待",
        keyword_check_ok : u"关键词检查通过",
        compile_ok : u"编译通过",
        run_ok : u"运行通过",
        output_check_ok : u"结果检查通过",
        
        
        keyword_checking : u"关键词检查",
        compiling : u"编译",
        running : u"运行",
        output_checking : u"结果检查",
             
        keyword_checked_error : u"禁用关键词",
        compiled_error : u"编译错误",
        runtime_error : u"运行时错误",
        memory_over_error : u"内存溢出错误",
        presentation_error : u"格式错误",
        wrong_answer : u"输出错误",
        
        fetched : u"等待处理",
        accept : u"通过",
               }
