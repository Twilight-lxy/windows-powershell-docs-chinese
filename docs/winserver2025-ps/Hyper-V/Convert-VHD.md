---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/convert-vhd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Convert-VHD
---

# 将VHD转换为其他格式

## 摘要
转换虚拟硬盘文件的格式、版本类型及块大小。

## 语法

```
Convert-VHD [-Path] <String> [-DestinationPath] <String> [-VHDType <VhdType>] [-ParentPath <String>]
 [-BlockSizeBytes <UInt32>] [-DeleteSource] [-AsJob] [-Passthru] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Convert-VHD` cmdlet 通过将数据从源虚拟硬盘文件复制到指定格式和版本类型的新虚拟硬盘文件来转换虚拟硬盘文件。格式由文件的扩展名决定，可以是 `.vhdx` 或 `.vhd`。转换过程是离线的；在开始转换操作时，虚拟硬盘必须处于未连接状态（即不能被系统使用）。

## 示例

### 示例 1
```
PS C:\> Convert-VHD -Path c:\test\testvhd.vhd -DestinationPath c:\test\testvhdx.vhdx
```

这个示例将源VHD转换为目标VHDX。由于文件格式由文件扩展名决定，而默认类型在没有指定类型时由源虚拟硬盘决定，因此目标虚拟硬盘将会是与源虚拟硬盘相同类型的VHDX格式磁盘。

### 示例 2
```
PS C:\> Convert-VHD -Path c:\test\child1vhdx.vhdx -DestinationPath c:\test\child1vhd.vhd -VHDType Differencing -ParentPath c:\test\parentvhd.vhd
```

这个示例将一个源差异磁盘（格式为VHDX）转换为目标差异磁盘（格式为VHD），并将目标差异磁盘连接到现有的父磁盘上。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。

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

### -BlockSizeBytes
指定转换后虚拟硬盘的数据块大小（以字节为单位）。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定一个或多个用于转换虚拟硬盘的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全限定的域名作为主机标识。默认值为本地计算机；可以使用 `localhost` 或点号（.）来明确表示本地计算机。

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

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -DeleteSource
指定在转换完成后删除源虚拟硬盘。

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

### -DestinationPath
指定转换后的虚拟硬盘文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ParentPath
指定用于生成差异备份虚拟硬盘文件的父路径。

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

### -Passthru
指定某个对象将被传递给流水线，该流水线用于表示转换后的虚拟硬盘。

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

### -Path
指定要转换的虚拟硬盘文件的路径。如果指定了文件名或相对路径，则转换后的硬盘文件路径将相对于当前工作目录进行计算。

```yaml
Type: String
Parameter Sets: (All)
Aliases: FullName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -VHDType
指定转换后的虚拟硬盘的类型。允许的值有 **Fixed**（固定大小）、**Dynamic**（动态扩展）和 **Differencing**（差分磁盘）。默认值由源虚拟硬盘的类型决定。

```yaml
Type: VhdType
Parameter Sets: (All)
Aliases:
Accepted values: Unknown, Fixed, Dynamic, Differencing

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上该cmdlet并没有被运行。

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

## 输出

### Microsoft.Vhd.PowerShell.VirtualHardDisk

## 备注

## 相关链接

