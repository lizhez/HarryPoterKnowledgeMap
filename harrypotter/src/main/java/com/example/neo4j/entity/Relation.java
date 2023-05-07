package com.example.neo4j.entity;

import lombok.Data;
import org.neo4j.ogm.annotation.*;

@Data
@RelationshipEntity(type = "关系")
public class Relation{
    @Id
    @GeneratedValue
    private Long id;
    @StartNode
    private Entity entity1;
    @EndNode
    private Entity entity2;
    @Property
    private String label;
}
