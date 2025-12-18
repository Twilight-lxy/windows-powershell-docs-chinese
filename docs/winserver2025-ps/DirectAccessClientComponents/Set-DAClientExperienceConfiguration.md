---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DAClientExperienceConfiguration.cdxml-help.xml
Module Name: DirectAccessClientComponents
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/directaccessclientcomponents/set-daclientexperienceconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-DAClientExperienceConfiguration
---

# Set-DAClientExperienceConfiguration

## 摘要
修改指定 DirectAccess 客户端用户体验的配置。

## 语法

### ByName（默认值）
```
Set-DAClientExperienceConfiguration [-PolicyStore <String>] [-GPOSession <String>]
 [[-CorporateResources] <String[]>] [[-IPsecTunnelEndpoints] <String[]>] [[-PreferLocalNamesAllowed] <Boolean>]
 [[-UserInterface] <Boolean>] [[-SupportEmail] <String>] [[-FriendlyName] <String>]
 [[-ManualEntryPointSelectionAllowed] <Boolean>] [[-GslbFqdn] <String>] [[-ForceTunneling] <ForceTunneling>]
 [[-CustomCommands] <String[]>] [[-PassiveMode] <Boolean>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject（cdxml）
```
Set-DAClientExperienceConfiguration -InputObject <CimInstance[]> [[-CorporateResources] <String[]>]
 [[-IPsecTunnelEndpoints] <String[]>] [[-PreferLocalNamesAllowed] <Boolean>] [[-UserInterface] <Boolean>]
 [[-SupportEmail] <String>] [[-FriendlyName] <String>] [[-ManualEntryPointSelectionAllowed] <Boolean>]
 [[-GslbFqdn] <String>] [[-ForceTunneling] <ForceTunneling>] [[-CustomCommands] <String[]>]
 [[-PassiveMode] <Boolean>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-DAClientExperienceConfiguration` cmdlet 用于修改 DirectAccess 客户端用户体验的指定配置属性。DirectAccess 客户端配置决定了用户界面的行为，以及用户可以使用的配置选项。

此cmdlet可用于更改存储在组策略对象（Group Policy Objects）中的配置属性。

## 示例

### 示例 1：禁用 DirectAccess 用户界面
```
PS C:\>Set-DAClientExperienceConfiguration -PolicyStore "Contoso\GPO1" -UserInterface "False"
```

这个cmdlet会禁用DirectAccess的用户界面。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。使用此参数来执行那些需要很长时间才能完成的任务。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Confirm
在运行 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -CorporateResources
配置 DirectAccess 客户端计算机用于检测连接性的测试。以字符串数组的形式输入该参数的值，每个值用双引号 (“”) 括起来，并用逗号分隔。每种测试类型使用以下格式：

HTTP测试：`"HTTP:http://computername"`

文件测试：`"FILE:\\fileserver\""`

ping测试：`"PING:testURL"`

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CustomCommands
配置管理员所需的任何自定义命令。这些自定义命令会包含在出现问题时生成的日志中。这些命令会在一个具有提升权限的 Windows PowerShell 控制台中依次执行。

字符串数组中的每个项目都必须是一个独立的命令。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 10
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForceTunneling
配置 DirectAccess 客户端计算机上的强制隧道设置。该参数的可接受值为：

- Enabled
- Disabled
- Default

By default, force tunneling is disabled.

```yaml
Type: ForceTunneling
Parameter Sets: (All)
Aliases:
Accepted values: Default, Enabled, Disabled

Required: False
Position: 9
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FriendlyName
Specifies the name of the DirectAccess deployment to be shown in the client computer user interface.
It is recommended that the name be 15 characters or less.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 6
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GPOSession
指定用于发送配置信息的组策略会话。您可以使用 *GPOSession* 与 **NetGPO** cmdlet 来汇总对某个组策略对象执行的多个操作。

*GPOSession* 不能与 *PolicyStore* 同时使用。

```yaml
Type: String
Parameter Sets: ByName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GslbFqdn
指定用于 DirectAccess 多站点客户端计算机的完全合格域名（FQDN）。客户端计算机将此 FQDN 解析为 IP 地址，并将该 IP 地址与入口点列表进行比较。客户端计算机使用匹配的入口点来建立连接。

请用双引号（“”）为 *GslbFqdn* 指定一个值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 8
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPsecTunnelEndpoints
配置用于 DirectAccess 的 IPsec 隧道端点。客户端计算机使用这些信息来验证 DirectAccess 服务器的可用性，并将这些信息呈现给用户。

请在双引号（“”）中为 *IPsecTunnelEndpoints* 指定值，用逗号分隔，格式如下：

“Ping: ipaddress”

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要传递给此 cmdlet 的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ManualEntryPointSelectionAllowed
该属性用于指定客户端计算机的用户是否可以更改用于 DirectAccess 连接的站点。如果 *ManualEntryPointSelectionAllowed* 被设置为 $True，则用户可以在用户界面中更改入口点配置；如果 *Manual EntryPointSelection Allowed* 被设置为 $False，则用户无法在用户界面中更改入口点配置。默认情况下，*ManualEntryPointSelectionAllowed* 的值为 $True。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 7
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
该cmdlet可以将交互式窗口中的项目作为输入数据传递给其他cmdlet。默认情况下，该cmdlet不会生成任何输出结果。不过，若要将这些项目传递到其他cmdlet中，请先点击鼠标选择所需的项目，再点击“确定”。同时支持使用Shift键或Ctrl键进行多选操作。

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

### -PassiveMode
用于控制 DirectAccess 客户端计算机上的被动模式设置。为了向用户报告 DirectAccess 的状态，DirectAccess 会定期执行一系列测试。当 *PassiveMode* 被设置为 $True 时，这些测试的频率会大大降低。但是，启用被动模式会导致客户端的响应速度变慢。

*PassiveMode* 的有效取值为 True 或 False。默认情况下，*PassiveMode* 被设置为 False，这也是推荐的做法。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 11
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PolicyStore
指定该cmdlet将配置信息存储到的策略存储库。

要将配置信息存储在组策略对象（Group Policy Object）中，请使用“Domain\GPOName”的格式指定GPO名称。

要将配置信息存储在计算机的本地组策略对象（GPO）中，请以“GPO:\<计算机名称\>”的格式指定该计算机的本地GPO名称。

*PolicyStore* 不能与 *GPOSession* 同时使用。

```yaml
Type: String
Parameter Sets: ByName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PreferLocalNamesAllowed
该字段用于指示用户是否可以断开 DirectAccess 连接。临时断开 DirectAccess 会使得名称解析策略表失效（即停止使用该策略表进行名称解析）。

`PreferLocalNames Allowed` 的有效取值为 `True` 或 `False`。如果将其设置为 `True`，用户可以断开与 DirectAccess 的连接。默认值为 `False`。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SupportEmail
配置用户界面中显示的电子邮件地址，以便用户发送日志和求助请求。要使日志记录功能正常工作，必须先配置 *SupportEmail*。

请以有效的电子邮件地址格式填写 *SupportEmail*。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 5
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的最大操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -UserInterface
启用或禁用接收该策略的客户端计算机上的 DirectAccess 用户界面。

*UserInterface* 的有效值为 True 或 False。将 *UserInterface* 设置为 False 会移除用户界面。默认情况下，*UserInterface* 被设置为 True。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/StandardCimv2/MSFTDAClientExperienceConfiguration
此cmdlet接受一个CIM对象作为输入，该对象包含DA客户端体验配置信息。

## 输出

### 无

## 备注

## 相关链接

[Get-DAClientExperienceConfiguration](./Get-DAClientExperienceConfiguration.md)

[Reset-DAClientExperienceConfiguration](./Reset-DAClientExperienceConfiguration.md)

