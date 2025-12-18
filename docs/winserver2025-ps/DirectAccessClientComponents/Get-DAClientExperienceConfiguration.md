---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DAClientExperienceConfiguration.cdxml-help.xml
Module Name: DirectAccessClientComponents
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/directaccessclientcomponents/get-daclientexperienceconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DAClientExperienceConfiguration
---

# Get-DAClientExperienceConfiguration

## 摘要
获取用于配置 DirectAccess 客户端用户体验的相关设置信息。

## 语法

```
Get-DAClientExperienceConfiguration [-PolicyStore <String>] [-GPOSession <String>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DAClientExperienceConfiguration` cmdlet 用于获取 DirectAccess 客户端用户体验的配置信息。该配置决定了用户界面的行为，以及用户可以使用的各种设置选项。

所有 **DAClientExperienceConfiguration** 命令符都有一个 ADMX 文件，也可以用来配置客户端体验设置。

## 示例

### 示例 1：从活动存储中获取 DirectAccess 客户端体验配置
```
PS C:\> Get-DAClientExperienceConfiguration -PolicyStore "ActiveStore"
```

此 cmdlet 从当前有效的策略存储中获取 DirectAccess 客户端体验配置信息。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -GPOSession
指定用于读取客户端体验配置信息的组策略会话。您可以使用 *GPOSession* 与 **NetGPO** cmdlet 来汇总对某个组策略对象执行的多个操作。

*GPOSession* 不能与 *PolicyStore* 同时使用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PolicyStore
指定cmdlet从中读取客户端体验配置信息的策略存储库。

要从组策略对象（Group Policy Object）中读取客户端体验配置信息，请使用“Domain\GPOName”的格式指定该GPO的名称。

要从计算机的本地组策略对象（GPO）中读取客户端体验配置信息，请以“GPO:\<计算机名称\>”的格式指定该计算机的本地GPO名称。

*PolicyStore* 不能与 *GPOSession* 同时使用。

*PolicyStore* 的默认值是 ActiveStore。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大数量。如果省略此参数或输入`0`，则Windows PowerShell®会根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最优限制值。这个限制仅适用于当前的cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance  
Microsoft.ManagementInfrastructure.CimInstance#root/StandardCimv2/MSFTDAClientExperienceConfiguration
此cmdlet返回一个CIM对象，其中包含DA客户端体验配置信息。

## 备注

## 相关链接

[Reset-DAClientExperienceConfiguration](./Reset-DAClientExperienceConfiguration.md)

[Set-DAClientExperienceConfiguration](./Set-DAClientExperienceConfiguration.md)

