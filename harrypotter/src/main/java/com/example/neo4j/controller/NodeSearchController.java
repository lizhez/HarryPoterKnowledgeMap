package com.example.neo4j.controller;

import com.example.neo4j.dao.EntityRelationShipRepository;
import com.example.neo4j.dao.EntityRepository;
import com.example.neo4j.dao.RelationRepository;
import com.example.neo4j.entity.Entity;
import com.example.neo4j.entity.EntityRelationShip;
import com.example.neo4j.entity.Relation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.LinkedList;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/searches")
public class NodeSearchController {

    @Autowired
    EntityRelationShipRepository entityRelationShipRepository;
    @Autowired
    RelationRepository relationRepository;
    @Autowired
    EntityRepository entityRepository;

    @GetMapping("/person/{id}")
    public List<Optional<Entity>> getById(@PathVariable Long id) {
        List<Optional<Entity>> entityList = new LinkedList<>();
        entityList.add(entityRepository.findById(id));
        if(entityRepository.findById(id+1)!=null)
            entityList.add(entityRepository.findById(id+1));
        else
            entityList.add(null);
        return entityList;
    }

    /*全部知识图谱：节点和关系*/
    @GetMapping("/allNodeRelations")
    public Iterable<EntityRelationShip> getAllNodeRelations() {
        Iterable<EntityRelationShip> relationRepositoryAll = entityRelationShipRepository.findAll();
        for (EntityRelationShip r : relationRepositoryAll) {
            String id1=null,id2=null;
            if(entityRepository.getNameByName(r.getSource())!=null)
                id1 = entityRepository.getNameByName(r.getSource()).getId().toString();
            if(entityRepository.getNameByName(r.getTarget())!=null)
                id2 = entityRepository.getNameByName(r.getTarget()).getId().toString();
            r.setSource(id1);
            r.setTarget(id2);
        }
        return relationRepositoryAll;
    }
    @GetMapping("/allNodes")
    public Iterable<Entity> getAllNodes() {
        Iterable<Entity> entityRepositoryAll = entityRepository.findAll();
        return entityRepositoryAll;
    }

    /*某个人的所有有关人物：节点和关系*/
    @GetMapping("/getRelationOfOne/nodes/{name}")
    public List<Entity> getNodesOfOne(@PathVariable String name) {
        List<Relation> relationList = relationRepository.getRelationOfOne(name);
        List<Entity> entityList = new LinkedList<>();
        for (Relation r : relationList) {
            int k=0;
            for (Entity e : entityList) {
                if(!e.getName().equals(r.getEntity2().getName()))
                    k++;
            }
            if(k== entityList.size())
                entityList.add(r.getEntity2());
        }
        entityList.add(entityRepository.getNameByName(name));
        return entityList;
    }
    @GetMapping("/getRelationOfOne/relations/{name}")
    public List<EntityRelationShip> getRelationOfOneRelations(@PathVariable String name) {
        List<Relation> relationList = relationRepository.getRelationOfOne(name);
        List<EntityRelationShip> relationShipRepositoryList = new LinkedList<>();
        for (Relation r : relationList) {
            EntityRelationShip relationShip = entityRelationShipRepository.getRelation(r.getEntity1().getName(),r.getEntity2().getName(),r.getLabel());
            relationShip.setSource(r.getEntity1().getId().toString());
            relationShip.setTarget(r.getEntity2().getId().toString());
            relationShipRepositoryList.add(relationShip);
        }
        return relationShipRepositoryList;
    }

    /*某两个人的关系：节点和关系*/
    @GetMapping("/getRelationBetweenTwo/nodes/{name1}/{name2}")
    public List<Entity> getNodesBetweenTwo(@PathVariable String name1,@PathVariable String name2) {
        List<Entity> entityList = new LinkedList<>();
        entityList.add(entityRepository.getNameByName(name1));
        entityList.add(entityRepository.getNameByName(name2));
        return entityList;
    }
    @GetMapping("/getRelationBetweenTwo/relations/{name1}/{name2}")
    public List<EntityRelationShip> getRelationBetweenTwo(@PathVariable String name1,@PathVariable String name2) {
        List<Relation> byName1 = relationRepository.getRelationBetweenTwo(name1,name2);
        List<EntityRelationShip> relationList = new LinkedList<>();
        for (Relation r : byName1) {
            EntityRelationShip relationShip = entityRelationShipRepository.getRelation(r.getEntity1().getName(),r.getEntity2().getName(),r.getLabel());
            relationShip.setSource(r.getEntity1().getId().toString());
            relationShip.setTarget(r.getEntity2().getId().toString());
            relationList.add(relationShip);
        }
        return relationList;
    }

    /*组织人数统计*/
    @GetMapping("/getCountOfClubs")
    public List<Integer> getCountOfClub() {
        String[] clubs = {"英国魔法部","食死徒","霍格沃茨魔法学校","凤凰社","邓布利多军"};
        List<Integer> counts = new LinkedList<>();
        for(int i=0;i< clubs.length;i++){
            List<EntityRelationShip> entityRelationShipList = entityRelationShipRepository.getRelationOfClub(clubs[i]);
            counts.add(entityRelationShipList.size());
        }
        return counts;
    }
    /*四大学院人数统计*/
    @GetMapping("/getCountOfSchools")
    public List<Integer> getCountOfSchool() {
        String[] schools = {"格兰芬多学院","斯莱特林学院","拉文克劳学院","赫奇帕奇学院"};
        List<Integer> counts = new LinkedList<>();
        for(int i=0;i< schools.length;i++){
            List<EntityRelationShip> entityRelationShipList = entityRelationShipRepository.getRelationOfClub(schools[i]);
            counts.add(entityRelationShipList.size());
        }
        return counts;
    }

    List<Relation> getRelationBetweenMany(String[] names,List<Relation> relationList){
        for(int i=0;i< names.length;i++){
            for(int j=0;j<names.length;j++){
                if(i!=j){
                    List<Relation> relation = relationRepository.getRelationBetweenTwo(names[i],names[j]);
                    for (Relation r : relation) {
                        relationList.add(r);
                    }
                }
            }
        }
        return relationList;
    }
    /*某个组织或学院的人员关系：节点，关系*/
    @GetMapping("/getRelationsOfSchool/nodes/{school}")
    public List<Entity> getNodeOfClub(@PathVariable String school) {
        List<EntityRelationShip> entityRelationShipList = entityRelationShipRepository.getRelationOfClub(school);
        String[] names = new String[entityRelationShipList.size()];
        int i=0;
        for (EntityRelationShip relation : entityRelationShipList) {
            names[i++]=relation.getSource();
        }
        List<Entity> entityList = new LinkedList<>();
        for (String name : names) {
            entityList.add(entityRepository.getNameByName(name));
        }
        return entityList;
    }
    @GetMapping("/getRelationsOfSchool/relations/{school}")
    public List<EntityRelationShip> getRelationOfClub(@PathVariable String school) {
        List<EntityRelationShip> entityRelationShips = new LinkedList<>();
        List<EntityRelationShip> entityRelationShipList = entityRelationShipRepository.getRelationOfClub(school);
        String[] names = new String[entityRelationShipList.size()];
        int i=0;
        for (EntityRelationShip relation : entityRelationShipList) {
            names[i++]=relation.getSource();
        }
        List<Relation> relationList = new LinkedList<>();
        getRelationBetweenMany(names,relationList);
        for (Relation r : relationList) {
            EntityRelationShip relationShip = entityRelationShipRepository.getRelation(r.getEntity1().getName(),r.getEntity2().getName(),r.getLabel());
            relationShip.setSource(r.getEntity1().getId().toString());
            relationShip.setTarget(r.getEntity2().getId().toString());
            entityRelationShips.add(relationShip);
        }
        return entityRelationShips;
    }

    /*许多节点间的关系：节点，关系*/
    @GetMapping("/getRelationBetweenMany/nodes/{name}")
    public List<Entity> getNodeBetweenMany(@PathVariable String name) {
        String[] names = name.split(",");
        List<Entity> entityList = new LinkedList<>();
        for (int i=0;i< names.length;i++) {
            entityList.add(entityRepository.getNameByName(names[i]));
        }
        return entityList;
    }
    @GetMapping("/getRelationBetweenMany/relations/{name}")
    public List<EntityRelationShip> getRelationBetweenMany(@PathVariable String name) {
        String[] names = name.split(",");
        List<Relation> relationList = new LinkedList<>();
        getRelationBetweenMany(names,relationList);

        List<EntityRelationShip> entityRelationShips = new LinkedList<>();
        for (Relation r : relationList) {
            EntityRelationShip relationShip = entityRelationShipRepository.getRelation(r.getEntity1().getName(),r.getEntity2().getName(),r.getLabel());
            relationShip.setSource(r.getEntity1().getId().toString());
            relationShip.setTarget(r.getEntity2().getId().toString());
            entityRelationShips.add(relationShip);
        }
        return entityRelationShips;
    }

    List<Relation> getRelationsOfSomebody(int i,String name,String[] relation,List<Relation> relationList){
        if(i<relation.length){
            List<Relation> byID = relationRepository.getRelations(name,relation[i]);
            i++;
            for (Relation r : byID) {
                relationList.add(r);
                if(i<relation.length)
                    getRelationsOfSomebody(i,r.getEntity2().getName(),relation,relationList);
            }
        }
        return relationList;
    }
    List<Entity> getRelationsOfSomebodyIsSomeone(int i,String name,String[] relation,List<Entity> entity){
        if(i<relation.length){
            List<Relation> byID = relationRepository.getRelations(name,relation[i]);
            i++;
            for (Relation r : byID) {
                if(i<relation.length)
                    getRelationsOfSomebodyIsSomeone(i,r.getEntity2().getName(),relation,entity);
                if (i==relation.length)
                    entity.add(r.getEntity2());

            }
        }
        return entity;
    }
    List<Entity> getNodesOfSomebody(int i,String name,String[] relation,List<Entity> entity){
        if(i<relation.length){
            List<Relation> byID = relationRepository.getRelations(name,relation[i]);
            i++;
            for (Relation r : byID) {
                int k=0;
                for (Entity e : entity) {
                    if(!e.getName().equals(r.getEntity2().getName()))
                        k++;
                }
                if(k== entity.size())
                    entity.add(r.getEntity2());
                if(i<relation.length)
                    getNodesOfSomebody(i,r.getEntity2().getName(),relation,entity);
            }
        }
        return entity;
    }

    /*查询某个人的复杂关系:节点，所有查询路径上的节点的关系，最终目标节点*/
    @GetMapping("/getRelationsOfSomebody/nodes/{name}/{relation}")
    public List<Entity> getNodesOfSomebodyList(@PathVariable String name,@PathVariable String relation) {
        String[] relations = relation.split(",");
        List<Entity> entityList = new LinkedList<>();
        getNodesOfSomebody(0,name,relations,entityList);
        entityList.add(entityRepository.getNameByName(name));
        return entityList;
    }
    @GetMapping("/getRelationsOfSomebody/relations/{name}/{relation}")
    public List<EntityRelationShip> getRelationsOfSomebodyList(@PathVariable String name,@PathVariable String relation) {
        String[] relations = relation.split(",");
        List<Relation> relationList = new LinkedList<>();
        getRelationsOfSomebody(0,name,relations,relationList);
        List<EntityRelationShip> entityRelationShips = new LinkedList<>();
        for (Relation r : relationList) {
            EntityRelationShip relationShip = entityRelationShipRepository.getRelation(r.getEntity1().getName(),r.getEntity2().getName(),r.getLabel());
            relationShip.setSource(r.getEntity1().getId().toString());
            relationShip.setTarget(r.getEntity2().getId().toString());
            entityRelationShips.add(relationShip);
        }
        return entityRelationShips;
    }
    @GetMapping("/getRelationsOfSomebodyIsSomeone/{name}/{relation}")
    public List<Entity> getRelationsOfSomebodyIsSomeoneList(@PathVariable String name,@PathVariable String relation) {
        String[] relations = relation.split(",");
        List<Entity> entityList = new LinkedList<>();
        getRelationsOfSomebodyIsSomeone(0,name,relations,entityList);
        return entityList;
    }

    /*页面二的加载数据*/
    @GetMapping("/getNodes")
    public List<Entity> getNodes() {
        String[] names = {"哈利·波特","赫敏·格兰杰","罗恩·韦斯莱","阿不思·邓布利多"
                ,"西弗勒斯·斯内普","米勒娃.麦格","鲁伯·海格","汤姆·马沃罗·里德尔"};
        List<Entity> entityList = new LinkedList<>();
        for (String name:names) {
            entityList.add(entityRepository.getNameByName(name));
        }
        return entityList;
    }

    @GetMapping("/getNodeByName/{name}")
    public Entity getNodeByName(@PathVariable String name) {
        return entityRepository.getNameByName(name);
    }
}
