---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DnsServerQueryResolutionPolicy_v1.0.0.cdxml-help.xml
Module Name: DnsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dnsserver/get-dnsserverqueryresolutionpolicy?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DnsServerQueryResolutionPolicy
---

# 获取 DNS 服务器查询解析策略

## 摘要
从DNS服务器获取用于查询解析的策略。

## 语法

### 服务器（默认设置）
```
Get-DnsServerQueryResolutionPolicy [[-Name] <String>] [-ComputerName <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 区域（Zone）
```
Get-DnsServerQueryResolutionPolicy [[-Name] <String>] [-ComputerName <String>] [-ZoneName] <String>
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DnsServerQueryResolutionPolicy` cmdlet 用于从域名系统（DNS）服务器获取查询解析相关的策略。可以通过名称指定一个区域来获取该区域的策略；如果未指定任何区域，此 cmdlet 将获取服务器级别的策略。

## 示例

### 示例 1：获取所有区域级别的策略
```
PS C:\> Get-DnsServerQueryResolutionPolicy -ZoneName "contoso.com" | Format-List *
```

此命令会获取名为“contoso.com”的区域的所有区域级策略。该命令使用了 **Format-List** cmdlet 来控制输出的形式。有关更多信息，请输入 `Get-Help Format-List`。

### 示例 2：获取特定区域的策略设置
```
PS C:\> Get-DnsServerQueryResolutionPolicy -Name "NorthAmericaPolicy" -ZoneName "contoso.com" | Format-List *
Action                : Allow
AppliesOn             : QueryProcessing
Condition             : And
Content               : {DnsServerPolicyContent}
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Zone
Name                  : NorthAmericaPolicy
ProcessingOrder       : 1
ZoneName              : contoso.com
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```

此命令用于获取名为 `NorthAmericaPolicy` 的区域级策略，该策略位于名为 `contoso.com` 的域中。

### 示例 3：获取所有服务器级别的策略
```
PS C:\> Get-DnsServerQueryResolutionPolicy | Format-List *
Action                : Ignore
AppliesOn             : QueryProcessing
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : DropPolicy
ProcessingOrder       : 1
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties

Action                : Ignore
AppliesOn             : QueryProcessing
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : DropPolicyMalicious
ProcessingOrder       : 2
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties

Action                : Ignore
AppliesOn             : QueryProcessing
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : DropPolicyQType
ProcessingOrder       : 3
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties

Action                : Allow
AppliesOn             : Recursion
Condition             : And
Content               : {DnsServerPolicyContent}
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : SplitBrainPolicy
ProcessingOrder       : 1
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```

这条命令可以获取所有服务器级别的策略。

### 示例 4：获取特定的服务器级别策略
```
PS C:\> Get-DnsServerQueryResolutionPolicy -Name "DropPolicy"
Name                                               ProcessingOrder                                    IsEnabled                                         Action
----                                               ---------------                                    ---------                                         ------
DropPolicy                                         1                                                  True                                              Ignore
```

这个命令用于获取名为 DropPolicy 的服务器级策略。

### 示例 5：显示所有服务器级别和区域级别的策略
```
PS C:\> $DnsServer = Get-DnsServer
PS C:\> $DnsServer.ServerPolicies | Format-List *
Action                : Ignore
AppliesOn             : QueryProcessing
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : DropPolicy
ProcessingOrder       : 1
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties

Action                : Ignore
AppliesOn             : QueryProcessing
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : DropPolicyMalicious
ProcessingOrder       : 2
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties

Action                : Ignore
AppliesOn             : QueryProcessing
Condition             : And
Content               :
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : DropPolicyQType
ProcessingOrder       : 3
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties

Action                : Allow
AppliesOn             : Recursion
Condition             : And
Content               : {DnsServerPolicyContent}
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Server
Name                  : SplitBrainPolicy
ProcessingOrder       : 1
ZoneName              :
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties

Action                : Allow
AppliesOn             : QueryProcessing
Condition             : And
Content               : {DnsServerPolicyContent}
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Zone
Name                  : AmericaPolicy
ProcessingOrder       : 1
ZoneName              : contoso.com
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties

Action                : Allow
AppliesOn             : QueryProcessing
Condition             : And
Content               : {DnsServerPolicyContent}
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Zone
Name                  : EuropePolicy
ProcessingOrder       : 2
ZoneName              : contoso.com
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties

Action                : Allow
AppliesOn             : QueryProcessing
Condition             : And
Content               : {DnsServerPolicyContent, DnsServerPolicyContent}
Criteria              : {DnsServerPolicyCriteria}
IsEnabled             : True
Level                 : Zone
Name                  : LBPolicy
ProcessingOrder       : 3
ZoneName              : contoso.com
PSComputerName        :
CimClass              : root/Microsoft/Windows/DNS:DnsServerPolicy
CimInstanceProperties : {Action, AppliesOn, Condition, Content...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties
```

第一个命令使用 `Get-DnsServer` cmdlet 获取当前 DNS 服务器的配置设置，并将这些值存储在 `$DnsServer` 变量中。

第二个命令通过使用管道运算符（pipeline operator），将存储在 `$DnsServer` 中的每个对象的 **ServerPolicies** 属性传递给 `Format-List` 命令。这个示例会显示服务器级别的策略和区域级别的策略。

### 示例 6：在 DNS 策略中显示相关标准
```
PS C:\> $Policy = Get-DnsServerQueryResolutionPolicy -Name "SamplePolicy" -ZoneName "contoso.com"
PS C:\> $Policy.Criteria
```

第一个命令获取一个策略对象，然后将其存储在 `$Policy` 变量中。

第二个命令会显示 `$Policy` 中的 `CriteriaType` 和 `Criteria` 的值。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行那些需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个远程DNS服务器。您可以指定一个IP地址，或者任何能够解析为IP地址的字符串，例如完全qualified domain name（FQDN）、主机名或NETBIOS名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要获取的策略的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ZoneName
指定用于获取区域级别策略的DNS区域的名称。该区域必须存在于DNS服务器上。

```yaml
Type: String
Parameter Sets: Zone
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#DnsServerPolicy[]

## 备注

## 相关链接

[Add-DnsServerQueryResolutionPolicy](./Add-DnsServerQueryResolutionPolicy.md)

[Remove-DnsServerQueryResolutionPolicy](./Remove-DnsServerQueryResolutionPolicy.md)

[Set-DnsServerQueryResolutionPolicy](./Set-DnsServerQueryResolutionPolicy.md)

[Get-DnsServer](./Get-DnsServer.md)

[Add-DnsServerZoneTransferPolicy](./Add-DnsServerZoneTransferPolicy.md)

