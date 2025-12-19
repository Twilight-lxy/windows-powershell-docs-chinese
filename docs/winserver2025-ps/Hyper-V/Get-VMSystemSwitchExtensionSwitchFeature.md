---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmsystemswitchextensionswitchfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMSystemSwitchExtensionSwitchFeature
---

# 获取虚拟机系统切换扩展的相关功能信息

## 摘要
获取Hyper-V主机上的交换机高级功能配置。

## 语法

```
Get-VMSystemSwitchExtensionSwitchFeature [-FeatureName <String[]>] [-FeatureId <Guid[]>]
 [-ExtensionName <String[]>] [-SystemSwitchExtension <VMSystemSwitchExtension[]>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

## 描述
`Get-VMSystemSwitchExtensionSwitchFeature` cmdlet 可用于获取一个或多个 Hyper-V 主机上虚拟交换机扩展所支持的交换机级功能。返回的函数对象将包含这些功能的默认值。该对象可通过 `Add-VMSwitchExtensionFeature` cmdlet 用于对特定端口应用相应的配置。

## 示例

### 示例 1
```
PS C:\> Get-VMSystemSwitchExtensionSwitchFeature
```

获取所有支持虚拟交换机级别功能的虚拟交换机扩展程序；这些功能可以在虚拟交换机上进行配置。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个 Hyper-V 主机，以便从这些主机中获取扩展程序中的交换机级功能。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机标识。默认值是本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExtensionName
指定用于获取开关级功能的扩展程序的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FeatureId
指定要检索的特征的唯一标识符。

```yaml
Type: Guid[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FeatureName
指定要检索的开关级（switch-level）功能的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SystemSwitchExtension
指定用于获取开关级（switch-level）功能的文件的扩展名。

```yaml
Type: VMSystemSwitchExtension[]
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

## 输出

## 备注

## 相关链接

