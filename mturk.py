import boto3,os,argparse
import pprint # just to make the output more readable; feel free to leave it out in your code

warning=" Use of this flag is strongly discouraged."


# let's add some arguments
parser=argparse.ArgumentParser(prog="AMT Launch Code")

parser.add_argument(
  '-t','--taskURL',
  help="the task URL in the following form 'https://foobar.com/task.html'"
)

parser.add_argument(
  '--live',
  action="store_true",
  help="Send the task to the real AMT marketplace.",
)

parser.add_argument(
  '--awsKey',
  help="Preferred AWS Key.{}".format(warning)
)

parser.add_argument(
  '--title',
  help="A custom title for the HIT (used in conjunction with the `create` flag)."
)

parser.add_argument(
  '--awsSecret',
  help="Your AWS Secret.{}".format(warning)
)

parser.add_argument(
  '-c',
  '--create',
  action="store_true",
  help="Create a *new* HIT."
)

parser.add_argument(
  '-l',
  '--listHITs',
  action="store_true",
  help="List extant HITs."
)

parser.add_argument(
  '-e',
  '--extend',
  help="Extend a HIT that's already in the marketplace."
)

parser.add_argument(
  '-g',
  '--getHIT',
  help="Get information about a specific HIT; needs a HIT ID."
)

args=parser.parse_args()


endpoint={
  'production': 'https://mturk-requester.us-east-1.amazonaws.com',
  'sandbox': 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
}

awsXMLSchema="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2006-07-14/ExternalQuestion.xsd"

external_content ="""
<ExternalQuestion xmlns="{awsXMLSchema}">
  <ExternalURL>{taskURL}</ExternalURL>
  <FrameHeight>400</FrameHeight>
</ExternalQuestion>
""".format(awsXMLSchema=awsXMLSchema,taskURL=args.taskURL)



quals=[
{
  'QualificationTypeId': "000000000000000000L0", # Amazon has a lot of arcane looking qualification types
  "Comparator": "GreaterThan",
  "IntegerValues": [85]
}]

client=boto3.client(
  service_name='mturk',
  region_name='us-east-1',
  aws_access_key_id=args.awsKey or os.environ['AMT_Example_key'], # => ~/.envariables
  aws_secret_access_key=args.awsSecret or os.environ['AMT_Example_secret'], # => ~/.envariables
  endpoint_url = endpoint['production'] if args.live else endpoint['sandbox']
)

if args.listHITs:
  response=client.list_hits()
  pprint.pprint(response)

if args.getHIT:
  response=client.get_hit(
    HITId=args.getHIT)
  pprint.pprint(response)


if args.create:
  response = client.create_hit(
    MaxAssignments = 20,
    LifetimeInSeconds = 60*60, # the HIT will only be active for 1 hour.
    AssignmentDurationInSeconds = (60*30), # this gives workers 30 minutes to complete it once they claim it.
    Reward ='0.50', # calculate the appropriate rate so people are getting paid fairly for their time.
    # if this task took 30 minutes to complete and i was paying $0.50, workers wouldn't even bother to do.
    Title = args.title or "some generic task, probably created accidentally",
    Keywords = 'question, answer, research, etc',
    Description = 'Answer a few survey questions',
    QualificationRequirements=quals,
    Question = external_content,
  )
