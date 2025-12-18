---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DAClientExperienceConfiguration.cdxml-help.xml
Module Name: DirectAccessClientComponents
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/directaccessclientcomponents/reset-daclientexperienceconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-DAClientExperienceConfiguration
---

# 重置 DAC 客户体验配置

## 摘要
将指定的DirectAccess客户端配置恢复到默认值。

## 语法

### 按名称排序（默认值）
```
Reset-DAClientExperienceConfiguration [-PolicyStore <String>] [-GPOSession <String>] [-CorporateResources]
 [-IPsecTunnelEndpoints] [-PreferLocalNamesAllowed] [-UserInterface] [-SupportEmail] [-FriendlyName]
 [-ManualEntryPointSelectionAllowed] [-GslbFqdn] [-ForceTunneling] [-CustomCommands] [-PassiveMode] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Reset-DAClientExperienceConfiguration -InputObject <CimInstance[]> [-CorporateResources]
 [-IPsecTunnelEndpoints] [-PreferLocalNamesAllowed] [-UserInterface] [-SupportEmail] [-FriendlyName]
 [-ManualEntryPointSelectionAllowed] [-GslbFqdn] [-ForceTunneling] [-CustomCommands] [-PassiveMode] [-PassThru]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Reset-DAClientExperienceConfiguration` cmdlet 将指定的 DirectAccess 客户端配置恢复为默认设置。

所有 **DAClientExperienceConfiguration** cmdlet 都有一个 ADMX 文件，该文件也可以用来配置这些设置。

## 示例

### 示例 1：重置客户端体验配置中的友好名称
```
PS C:\>Reset-DAClientExperienceConfiguration -PolicyStore "Contoso\GPO1" -FriendlyName "Traveling Policy"
```

此cmdlet用于重置客户端体验配置的友好名称。

## 参数

### -AsJob
以后台作业的方式运行该 cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
在运行cmdlet之前，会提示您进行确认。

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
将指定配置的 `CorporateResources` 属性重置为未配置的状态。

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

### -CustomCommands
将指定配置的 `CustomCommands` 属性重置为未配置的状态。

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

### -ForceTunneling
将指定配置的ForceTunneling属性重置为未配置的状态。

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

### -FriendlyName
将指定配置的 FriendlyName 属性重置为未配置的状态。

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

### -GPOSession
指定用于发送配置信息的组策略会话。您可以使用 *GPOSession* 与 **NetGPO** 命令集，来汇总对某个组策略对象执行的多个操作。

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
将指定配置中的 GslbFqdn 属性重置为未配置的状态。

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

### -IPsecTunnelEndpoints
将指定配置的 `IPsecTunnelEndpoints` 属性重置为未配置的状态。

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

### -InputObject
指定在管道命令中使用的输入对象。

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
将指定配置的 `ManualEntryPointSelectionAllowed` 属性重置为未配置的状态。

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

### -PassThru
将交互式窗口中的项目作为输入发送到其他cmdlet中。默认情况下，此cmdlet不会生成任何输出。但是，要将交互式窗口中的项目发送到管道中，请先单击以选择这些项目，然后单击“确定”。支持使用Shift键和Ctrl键进行选择。

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
将指定配置的 `PassiveMode` 属性重置为未配置的状态。

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

### -PolicyStore
指定该cmdlet将重置配置属性添加到的策略存储位置。

要将重置配置属性添加到组策略对象（Group Policy Object）中，请使用“Domain\GPOName”格式指定该GPO的名称。

要将重置配置属性添加到计算机的本地组策略对象（Local Group Policy Object，简称GPO）中，请以“GPO:<计算机名称>”的格式指定该计算机的本地GPO名称。

**PolicyStore** 不能与 **GPOSession** 同时使用。

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
将指定配置的 `PreferLocalNames Allowed` 属性重置为未配置的状态。

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

### -SupportEmail
将指定配置的 `SupportEmail` 属性重置为未配置的状态。

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

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机。

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
将指定配置的 `UserInterface` 属性重置为未配置的状态。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上并没有运行这个cmdlet。

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

[Set-DAClientExperienceConfiguration](./Set-DAClientExperienceConfiguration.md)

