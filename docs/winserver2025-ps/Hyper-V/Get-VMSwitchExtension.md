---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmswitchextension?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMSwitchExtension
---

# Get-VMSwitchExtension

## 摘要
获取应用于虚拟交换机的扩展功能信息。

## 语法

### SwitchName（默认值）
```
Get-VMSwitchExtension [-VMSwitchName] <String[]> [[-Name] <String[]>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

### SwitchObject
```
Get-VMSwitchExtension [-VMSwitch] <VMSwitch[]> [[-Name] <String[]>] [<CommonParameters>]
```

## 描述
`Get-VMSwitchExtension` cmdlet 可以获取一个或多个虚拟交换机上的扩展功能。这些扩展功能可能属于不同的类型，并且可以被启用或禁用。输出结果可以根据扩展功能的类型进行过滤。返回的扩展对象中不包含用于表示各种功能的嵌入对象，也不包含功能 ID 的数组。

## 示例

### 示例 1
```
PS C:\> Get-VMSwitch InternalSwitch | Get-VMSwitchExtension
```

获取所有可供虚拟交换机InternalSwitch使用的虚拟交换机扩展功能。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: SwitchName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于检索扩展程序的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全 Qualified Domain Name（FQDN）来标识这些主机。默认值为本地计算机。可以使用 “localhost” 或点号（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: SwitchName
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
Parameter Sets: SwitchName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要检索的扩展名的名称。

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

### -VMSwitch
指定用于获取扩展程序的虚拟交换机。

```yaml
Type: VMSwitch[]
Parameter Sets: SwitchObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSwitchName
指定用于获取扩展程序的虚拟交换机的名称。

```yaml
Type: String[]
Parameter Sets: SwitchName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMSwitchExtension

## 备注

## 相关链接

