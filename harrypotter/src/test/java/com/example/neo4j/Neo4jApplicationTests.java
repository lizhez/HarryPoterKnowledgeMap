package com.example.neo4j;

import com.example.neo4j.dao.EntityRelationShipRepository;
import com.example.neo4j.dao.EntityRepository;
import com.example.neo4j.dao.RelationRepository;
import com.example.neo4j.entity.Entity;
import com.example.neo4j.entity.EntityRelationShip;
import com.example.neo4j.entity.Relation;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.LinkedList;
import java.util.List;
import java.util.Optional;

@SpringBootTest
class Neo4jApplicationTests {

	@Autowired
	EntityRelationShipRepository entityRelationShipRepository;
	@Autowired
	RelationRepository relationRepository;
	@Autowired
	EntityRepository entityRepository;

	@Test
	void getByID() {
		Optional<EntityRelationShip> byID = entityRelationShipRepository.findById(7200L);
		System.out.println(byID);
	}
	@Test
	void getAllRelations() {
		Iterable<EntityRelationShip> byID = entityRelationShipRepository.findAll();
		for (EntityRelationShip relation : byID) {
			System.out.println(relation.getSource() + "--"+relation.getLabel()+"-->" + relation.getTarget());
		}
	}
	@Test
	void getAllNodes() {
		Iterable<Entity> byID = entityRepository.findAll();
		for (Entity node : byID) {
			System.out.println(node.toString());
		}
	}

	@Test
	void getRelationBetweenTwo() {
		List<Relation> byID1 = relationRepository.getRelationBetweenTwo("哈利·波特","赫敏·格兰杰");
		List<Relation> byID2 = relationRepository.getRelationBetweenTwo("赫敏·格兰杰","哈利·波特");
		for (Relation relation : byID1) {
			Entity sNode = relation.getEntity1();
			Entity eNode = relation.getEntity2();
			System.out.println(sNode.getName() + "--"+relation.getLabel()+"-->" + eNode.getName());
		}
		for (Relation relation : byID2) {
			Entity sNode = relation.getEntity1();
			Entity eNode = relation.getEntity2();
//			System.out.println(sNode.getName() + "--"+relation.getRelation()+"-->" + eNode.getName());
			System.out.println(byID2);
		}
	}

	@Test
	void getRelationOfOne() {
		List<Relation> byID1 = relationRepository.getRelationOfOne("哈利·波特");
		List<Entity> entityList = new LinkedList<>();
		for (Relation r : byID1) {
			int k=0;
			for (Entity e : entityList) {
				if(!e.getName().equals(r.getEntity2().getName()))
					k++;
			}
			if(k== entityList.size())
				entityList.add(r.getEntity2());
		}
		for (Entity entity:entityList) {
			System.out.println(entity.getName());
		}
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

	@Test
	void getRelations() {
		String[] r ={"内兄","妻子","嫂子"};

		List<Entity> e = new LinkedList<>();
		getRelationsOfSomebodyIsSomeone(0,"哈利·波特",r,e);
		System.out.println(e);

		List<Relation> relationList = new LinkedList<>();
		getRelationsOfSomebody(0,"哈利·波特",r,relationList);
		for (Relation relation : relationList) {
			Entity sNode = relation.getEntity1();
			Entity eNode = relation.getEntity2();
			System.out.println(sNode.getName() + "--"+relation.getLabel()+"-->" + eNode.getName());
		}

	}

	@Test
	void getRelationBetweenMany() {
		String[] names ={"哈利·波特","赫敏·格兰杰","罗恩·韦斯莱"};
		List<Relation> relationList = new LinkedList<>();
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
		for (Relation relation : relationList) {
			Entity sNode = relation.getEntity1();
			Entity eNode = relation.getEntity2();
			System.out.println(sNode.getName() + "--"+relation.getLabel()+"-->" + eNode.getName());
		}
	}

	@Test
	void getCountOfSchool() {
		String[] schools = {"格兰芬多学院","斯兰特林学院","拉文克劳学院","赫奇帕奇学院"};
		List<Integer> counts = new LinkedList<>();
		for(int i=0;i< schools.length;i++){
			List<EntityRelationShip> entityRelationShipList = entityRelationShipRepository.getRelationOfClub(schools[i]);
			counts.add(entityRelationShipList.size());
		}
	}

	@Test
	void g() {
		List<EntityRelationShip> entityRelationShipList = entityRelationShipRepository.getRelationOfClub("斯莱特林学院");
		String[] names = new String[entityRelationShipList.size()];
		int i=0;
		for (EntityRelationShip relation : entityRelationShipList) {
			names[i++]=relation.getSource();
			System.out.println(names[i-1]);
		}
	}

	@Test
	void f() {
		List<Relation> relationList = relationRepository.getRelationOfOne("哈利·波特");
		List<EntityRelationShip> relationShipRepositoryList = new LinkedList<>();
		for (Relation r : relationList) {
			System.out.println(r.getEntity1().getName());
			System.out.println(r.getEntity2().getName());
			System.out.println(r.getLabel());
			EntityRelationShip relationShip = entityRelationShipRepository.getRelation(r.getEntity1().getName(),r.getEntity2().getName(),r.getLabel());
			System.out.println(relationShip);
			relationShipRepositoryList.add(relationShip);
		}
	}

	@Test
	void a() {
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
		System.out.println("ffff");
	}

	@Test
	void b() {
		List<Optional<Entity>> entityList = new LinkedList<>();
		entityList.add(entityRepository.findById(9026L));
//		if(entityRepository.findById(9027L)!=null)
//			entityList.add(entityRepository.findById(9027L));
//		else
			entityList.add(null);
		System.out.println("ffff");
	}

}
