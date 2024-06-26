const { Builder, By, Key, until } = require('selenium-webdriver')
const assert = require('assert')

describe('Case3', function() {
  this.timeout(30000)
  let driver
  let vars
  
  beforeEach(async function() {
    driver = await new Builder().forBrowser('chrome').build()
    vars = {}
  })
  
  afterEach(async function() {
    await driver.quit();
  })
  
  it('OpenLoginPage', async function() {
    await driver.get("http://automationpractice.com/")

    if ((await driver.findElements(By.xpath("//a[contains(text(),\'Sign out\')]"))).length > 0) {
      await driver.findElement(By.linkText("Sign out")).click()
    }
	
    await driver.findElement(By.linkText("Sign in")).click()
    assert(await driver.getTitle() == "Login - My Store")
  })
  
  it('TryAuthoriseUseOnlyLogin', async function() {
    await driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    await driver.findElement(By.id("email")).sendKeys("ankl_npuedu@example.com")
    await driver.findElement(By.css("#SubmitLogin > span")).click()
	
    await driver.wait(until.elementIsVisible(await driver.findElement(By.css("#center_column > .alert"))), 10000)
    {
      const elements = await driver.findElements(By.xpath("//li[contains(.,\'Password is required.\')]"))
      assert(elements.length)
    }
  })
})
