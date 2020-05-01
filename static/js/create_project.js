class Project{
    constructor(name,languaje,manager){
        this.name=name;
        this.languaje=languaje;
        this.manager=manager;
    }
}

class UI{


    //Añadir nuevo proyecto
    addProject(project){
         const projectList = document.getElementById('project-list')
         const element = document.createElement('div');
         element.innerHTML= `
            <div class="card text-center mb-4">
                <div class="card-body">
                    <strong>Project name</strong>:${project.name}
                    <strong>Languaje</strong>:${project.languaje}
                    <strong>Prodject manager</strong>:${project.manager}
                    <a href="#" class="btn btn-danger" name="delete"> Delete</a>
                </div>
            </div>
         `;
         projectList.appendChild(element);
         
//resetear formulario
    
    }
    resetForm(){
        document.getElementById('project-form').reset();
    }



//eliminar proyecto

    deleteProject(element){
        if(element.name === 'delete'){
            element.parentElement.parentElement.parentElement.remove();
            this.showMessage('Product Deleted Sucessfully','info');
        }
    }




//mostrar mensajes

    showMessage(message,cssClass){
        const div = document.createElement('div');
        
        div.className=`alert alert-${cssClass} mt-4`;
        div.appendChild(document.createTextNode(message));

        const container = document.querySelector('.container');
        const project = document.querySelector('#Project');

        container.insertBefore(div, project);
        setTimeout(function(){
            document.querySelector('.alert').remove();
        },2000);
    }
}






document.getElementById('project-form').addEventListener('submit', function(e){
    const name = document.getElementById('name').value;
    const languaje = document.getElementById('languaje').value;
    const manager = document.getElementById('manager').value;
    const project = new Project(name,languaje,manager)
    const ui = new UI();

    if (name === '' || languaje === '' || mager === ''){
        return ui.showMessage('!Error! Complete Fields Please','danger')
    }
    ui.addProject(project);
    ui.resetForm();
    ui.showMessage('Project Added Successfully','success');

    e.preventDefault();
});

document.getElementById('project-list').addEventListener('click', function(e){
    const ui = new UI();
    ui.deleteProject(e.target);
});