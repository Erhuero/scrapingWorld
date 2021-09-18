Cypress.Commands.add("SignIn", () => {//forcage de commandes avec le meme code que dans les spec.js
    
        cy.visit('/#/login')//lance le programme, urlBase est le prefixe de l'adresse qui se trouve dans le fichier command.js
        cy.title().should('eq', 'Conduit')//nous donne le titre et verifie si il est correct
        cy.location('protocol').should('eq', 'https:')//verifie si l'addresse est bien en https
        //cy.get('input[type="email"]').type('constantin.chtanko@gmail.com')
        //cy.get('input[type="password"]').type('Osmium.222')
        //cy.get('.btn').contains('Sign in').should('be.visible').click() //should ajoute un message dans les logs .btn fait reference au bouton d'inscription

        cy.get('form').within(($form) => {//on recupere l'element form puis on cherche les elements "within" dans les elements
            //la recherche se fait dans le element form et pas dans le document entier
            cy.get('input[type="email"]').type('constantin.chtanko@gmail.com')
            cy.get('input[type="password"]').type('Osmium.222')
            cy.get('.btn').contains('Sign in').should('be.visible').click()
            cy.root().submit()//valide le form

        })
        
        cy.contains('Your Feed', { timeout: 10000 }).should('be.visible')//verifie si le mot Your Feed est bien present sur la page
        //timeout laisse la page pendant quelques secondes et vérifie si le mot Your Feed existe bien
 

})