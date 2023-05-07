package com.example.neo4j.entity;

import lombok.Data;
import org.neo4j.ogm.annotation.*;


import java.io.Serializable;

@Data
@NodeEntity(label = "entityRelation")
public class EntityRelationShip{
    @Id
    @GeneratedValue
    private Long id;
    @Property
    private String source;
    @Property
    private String target;
    @Property
    private String label;
}
