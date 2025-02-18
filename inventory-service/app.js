const express = require('express')
const {Eureka} = require("eureka-js-client")
/*const EurekaClient = require("eureka-js-client")
const Eureka = EurekaClient.Eureka*/

const app = express();
const port = 3000;

const router = express.Router()

router.get('/inventory', (req, res)=>{
    res.json({
        items: ['Milk', 'Eggs', 'Bread'],
        message: 'Welcome to the inventory service'
    })
})

// application context
app.use('/inventory-service', router)

const eurekaClient = new Eureka({
    instance: {
        instanceId: "inventory-service",
        app: "INVENTORY-SERVICE",
        hostName: "localhost",
        ipAddr: "127.0.0.1",
        port: {
            $: port,   // Ensure it matches app's running port
            "@enabled": true,
        },
        vipAddress: "inventory-service",
        dataCenterInfo: {
            "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
            name: "MyOwn",
        },
    },
    eureka: {
        host: "localhost",
        port: 8761,
        //servicePath: "/eureka/apps/",
    },
});

app.listen(port, ()=>{
    console.log(`inventory service running at port: ${port}`)

    eurekaClient.start((error)=>{
        if (error){
            console.error("Failed to register Eureka !")
        }else {
            console.log("Successfully registered with Eureka")
        }
    })
})