Batch-download
--

- This is a simple script.Those module provide some method to fetch and download data from web page.这是简单的脚本程序，你可以利用它自动爬取并批量的下载网页上的资源。

### feature

- Provide generic text file like txt,html,xml etc.支持常见的文本资源。
- Provide generic binary file like jpg,png,bmp etc.支持常见的二进制资源。
- Custom dir for save download file.自定义下载保存目录。  
- Provide make dir of download-files for each page ，or make dir for all page.支持每个页面独立保存为每个目录，或者全部保存为一个目录。
- Provide custom split downloading with second.支持每秒间隔下载自定义。
- Provide custom sleep time and number of times of retry or exit when connect failed.支持自定义连接失败是否重试，以及次数和间隔。
- Provide special handling of the first url of pages.支持首页URL特殊处理。
- Provide make up 0 in front of number of page like 1 and 01.支持页数前面加0，如9变为09。
- Provide generate referer by url of current page.支持根据当前页面设置referer。
- Output log by console.控制台输出日志。
