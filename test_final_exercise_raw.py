
from selenium import webdriver
from selenium.webdriver.common.by import By

from homepage import HomePage

class TestDemo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_demo(self):
    self.driver.get("https://tdd-detroid.onrender.com/")
    self.driver.set_window_size(970, 555)

    home_page = HomePage(self.driver)
    home_page.wait_page_load()   
    
    home_page.add_student(student="raquel leao")
    assert (
      "INFO Added student id: 1, Name: raquel leao" 
      in self.driver.find_element(By.CSS_SELECTOR, ".py-p").text 
    )

    home_page.add_course_temp(course="software")
    assert (
      "INFO Added student id: 1, Name: raquel leao" 
      in self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(2)").text 
    )

    home_page.add_student_to_course()
    assert (
      "INFO Added student id: 1, Name: raquel leao"
      in self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(3)").text 
    )

    home_page.subcribe_discipline_to_course()
    assert (
      "FAIL Necessários 3 cursos para se criar a primeira matéria"
      in self.get_first_log() 
    )
  
    home_page.add_course_temp(course="teste de software")
    home_page.add_course_temp(course="teste de aplicacao")

    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()

    assert (
      "INFO Added discipline id: 1, Name: teste, Course: 1" 
      in self.get_first_log() 
    )

    home_page.add_discipline_temp(discipline = "UX")
    home_page.add_discipline_temp(discipline = "cypress")

    home_page.subscribe_student_to_discipline(1, 1)

    assert (
      "WARN Aluno deve se inscrever em 3 materias no minimo" 
      in self.get_first_log() 
    )

    home_page.subscribe_student_to_discipline(1,2)
    home_page.add_discipline_temp("automacao")
    home_page.subscribe_student_to_discipline(1,4)

    self.driver.close()

  def get_first_log(self):
      return self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").text

  def get_first_log(self):
      return self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").text

  def get_first_log(self):
      return self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").text


  

  
