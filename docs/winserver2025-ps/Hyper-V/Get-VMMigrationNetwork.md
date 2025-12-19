---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmmigrationnetwork?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMMigrationNetwork
---

# Get-VMMigrationNetwork

## 摘要
获取用于一台或多台虚拟机迁移的网络信息。

## 语法

```
Get-VMMigrationNetwork [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [[-Subnet] <String[]>] [-Priority <UInt32[]>] [<CommonParameters>]
```

## 描述
`Get-VMMigrationNetwork` cmdlet 可获取为迁移到一个或多个虚拟机主机而添加的网络信息。

## 示例

### 示例 1
```
PS C:\> Get-VMMigrationNetwork
```

获取所有需要迁移到的本地虚拟机主机上的网络信息。

### 示例 2
```
PS C:\> Get-VMMigrationNetwork -Priority 8
```

获取所有要迁移到本地虚拟机主机上的网络，并为这些网络设置优先级为 8。

### 示例 3
```
PS C:\> Get-VMMigrationNetwork 192.168.*
```

获取所有用于迁移的网络信息，这些网络包含以“192.168.”开头的子网。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 获得的会话对象）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个 Hyper-V 主机，用于从中检索用于迁移的网络信息。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机标识。默认值为本地计算机。可以使用 `localhost` 或`.` 明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
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

### -Priority
指定要检索的网络的优先级。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Subnet
指定一个字符串，该字符串表示一个IPv4或IPv6子网掩码，用于标识需要检索的网络。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV POWERShell.VMMigrationNetwork

## 备注

## 相关链接

