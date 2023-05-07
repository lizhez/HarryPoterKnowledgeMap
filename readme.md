有关项目文件夹的内容说明：
data -- 文件夹是构建知识图谱的源数据
人名、人物关系、图片收集与处理 -- 文件夹
person_info -- 文件夹是有关人物信息数据的收集和处理
知识图谱 -- 文件夹是构建的知识图谱导出的文件，以及整个知识图谱的预览
harrypotter -- 文件夹是后端项目，使用srpingboot+neo4j，环境是jdk8
vue_neo4j -- 文件夹是前端项目，使用vue2+jQuery组件+element ui组件+echarts图表

数据库构建的语句：
load csv from 'file:///harrypotterdata.csv' as line
create (:entityRelation {source:line[0],target:line[1],label:line[2]})
load csv from 'file:///harrypotternode.csv' as line
create (:entity {name:line[0],meta:line[1],nickname:line[2],player:line[3],appearance:line[4],birthday:line[5],magicstick:line[6],sex:line[7],character:line[8],url:line[9],video:line[10],images:line[11]})
match (n:entity),(m:entityRlation),(s:entity) where n.name=m.source and s.name=m.target
create (n)-[r:关系{label:m.relation}]->(s)
return n.name,m.label,s.name

知识图谱查询搜索的查询词建议：
单人关系：哈利·波特
双人关系：哈利·波特,赫敏·格兰杰；赫敏·格兰杰哈利·波特
复杂关系查询：内兄,妻子,嫂子
多人关系查询：哈利·波特,赫敏·格兰杰,罗恩·韦斯莱
数据库中最后一个实体：齐格蒙特·巴奇