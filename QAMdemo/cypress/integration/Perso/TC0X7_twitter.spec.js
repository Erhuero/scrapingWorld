describe("Login", function () {
    it('Sign in', function () {
        cy.visit('https://twitter.com/login')
        cy.get('input[type="text"]').type('BourbierLive')
        cy.get('input[type="password"]').type('Qbe8MKa6*')
        cy.get('span.r-qvutc0').contains('Se connecter',  {timeout:10000}).should('be.visible').click()

        })
        it('Envoyer un message', function() {
            cy.get('.a').contains('Notifications').click()//appuie sur le menu new post
            //cy.hash().should('include','#/editor')//verifie qu'on est bien sur la bonne page, le hash url de la page activeS
            //cy.location('hash').should('include','#/editor') //même chose que la ligne precedente
            //cy.get('input[placeholder="Article Title"]').type('Cheekiii breakiii')//trouve l'entree du titre et marque le message
            //cy.get('input[placeholder="What\'s this article about?"]').type('Daym bro !')//slash inverse pour eviter l'apostrophe
            //cy.get('textarea[placeholder="Write your article (in markdown)"]').type('Fucking bourbier around here bruh')
            //cy.get('input[placeholder="Enter tags"]').type("daym")
            //cy.get('.btn').contains('Publish Article').click()
            //cy.url().should('include','article')//pas besoin de hastag avec url(), retourne l'url complet
        })
  })
