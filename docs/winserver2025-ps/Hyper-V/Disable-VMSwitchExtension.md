---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/disable-vmswitchextension?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-VMSwitchExtension
---

# 禁用 VMSwitch 扩展程序

## 摘要
禁用一台或多台虚拟交换机上的扩展功能。

## 语法

### ExtensionName（默认值）
```
Disable-VMSwitchExtension [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-Name] <String[]> [<CommonParameters>]
```

### ExtensionNameSwitchName
```
Disable-VMSwitchExtension [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-Name] <String[]> [-VMSwitchName] <String[]> [<CommonParameters>]
```

### ExtensionNameSwitchObject
```
Disable-VMSwitchExtension [-Name] <String[]> [-VMSwitch] <VMSwitch[]> [<CommonParameters>]
```

### ExtensionObject
```
Disable-VMSwitchExtension [-VMSwitchExtension] <VMSwitchExtension[]> [<CommonParameters>]
```

## 描述
`Disable-VMSwitchExtension` cmdlet 可以禁用一个或多个虚拟交换机上的一个或多个扩展功能。你可以运行 `Get-VMSystemSwitchExtension` 命令来查看系统中安装的虚拟交换机扩展功能列表。

## 示例

### 示例 1
```
PS C:\> Disable-VMSwitchExtension -VMSwitchName "Internal Switch" -Name "Microsoft Windows Filtering Platform"
```

在内部交换机（Internal Switch）上禁用WFP（“Microsoft Windows Filtering Platform”）。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: ExtensionName, ExtensionNameSwitchName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个需要禁用该扩展程序的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行指定。默认值是本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: ExtensionName, ExtensionNameSwitchName
Aliases: PSComputerName

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
Parameter Sets: ExtensionName, ExtensionNameSwitchName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要禁用的扩展名的名称。

```yaml
Type: String[]
Parameter Sets: ExtensionName, ExtensionNameSwitchName, ExtensionNameSwitchObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMSwitch
指定要禁用该扩展程序的虚拟交换机。

```yaml
Type: VMSwitch[]
Parameter Sets: ExtensionNameSwitchObject
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSwitchExtension
指定要禁用的文件扩展名。

```yaml
Type: VMSwitchExtension[]
Parameter Sets: ExtensionObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSwitchName
指定要禁用该扩展程序的交换机的名称。

```yaml
Type: String[]
Parameter Sets: ExtensionNameSwitchName
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMSwitchExtension

## 备注

## 相关链接

